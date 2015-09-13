from splinter import Browser
browser=Browser('firefox')
browser.visit('http://ldma.robi.com.bd/')

class ldma_Update:

    def __init__(self,user_email,user_pass):
        self.user_email=user_email
        self.user_pass=user_pass
        browser.fill('username',self.user_email)
        browser.fill('password',self.user_pass)
        browser.find_by_value('Sign In').click()
    def openLinks(self,link_code):
        self.link=link_code
        browser.find_link_by_partial_text('Links').click()
        browser.find_by_id('statusType').select('0')
        browser.fill("search",link_code)
        browser.find_by_value('Search').click()
        browser.find_link_by_partial_text(self.link).click()

    def site_info(self):
        s1= browser.find_by_id("site1Name").value
        s2= browser.find_by_id("site2Name").value
        return s1+" to "+s2

    def site_codes(self):
        s1=browser.find_by_id("siteID1").value
        s2=browser.find_by_id("siteID2").value
        return (s1,s2)

    def near_e1_route(self,main_port,NE_ms,slot,port):
        main_slot1=[]
        nearSlot=[]
        nearPort=[]
        try:
            browser.find_by_name('allocateE1Data').click()
            for ports in main_port:
                print ports
                main_slot1+=['slotM1'+str(ports)]
                nearSlot+=['slotL1'+str(ports)]
                nearPort+=['portL1'+str(ports)]



            if len(main_port)==len(NE_ms):
                for i in range(0,len(main_port)):
                    browser.fill(main_slot1[i],NE_ms[i])
                    browser.fill(nearSlot[i],slot[i])
                    browser.fill(nearPort[i],port[i])
            else:
                print "info missing "



        except AttributeError:
            print "ca't open e1 route window"
            pass


    def far_e1_route(self,main_port,FE_ms,slot,port):
        main_slot1=[]
        nearSlot=[]
        nearPort=[]
        try:
            for ports in main_port:
                print ports
                main_slot1+=['slotM2'+str(ports)]
                nearSlot+=['slotL2'+str(ports)]
                nearPort+=['portL2'+str(ports)]



            if len(main_port)==len(FE_ms):
                for i in range(0,len(main_port)):
                    browser.fill(main_slot1[i],FE_ms[i])
                    browser.fill(nearSlot[i],slot[i])
                    browser.fill(nearPort[i],port[i])
            else:
                print "info missing "



        except AttributeError:
            print "ca't open e1 route window"
            pass

    def change_status(self,main_port):
        for i in range(0,len(main_port)):
            browser.find_by_id('processedStatus'+str(main_port[i])).select('16')


    
    def amm_update(self,NearEnd,FarEnd):
        """ cases
                20P A EX-20P
                """
        try:
            s=""
            l=NearEnd.split(" ")
            s=l[0]
            l=s.split("_")
            NearEnd=l[0]
            print NearEnd
            
            l=FarEnd.split(" ")
            s=l[0]
            l=s.split("_")
            FarEnd=l[0]
            print FarEnd
            
            pos=NearEnd.find("-")
            
            
            if(pos!=-1):
                NearEnd="AMM"+NearEnd[pos+1:]
                print NearEnd
                browser.find_by_id('ammTypeSite1').select('Existing')
                browser.find_by_id('nodalefield1').select(NearEnd)
                

            else:
                NearEnd="AMM"+NearEnd
                print NearEnd
                browser.find_by_id('ammTypeSite1').select('New')
                browser.find_by_id('nodalefield1').select(NearEnd)


       
            pos=FarEnd.find("-")
            if(pos!=-1):

                FarEnd="AMM"+FarEnd[pos+1:]
                print FarEnd
                browser.find_by_id('ammTypeSite2').select('Existing')
                browser.find_by_id('nodalefield1Site2').select(FarEnd)

            else:
                FarEnd="AMM"+FarEnd
                print FarEnd
                browser.find_by_id('ammTypeSite2').select('New')
                browser.find_by_id("nodalefield1Site2").select(FarEnd)
        except  AttributeError:
            print "NOT UPDATED"


    def ip_update(self,NearEnd, FarEnd):                #tuple object as input (IP info, subnet mask, ospf area)
        try:
            #Near End
            l=NearEnd.split("_")
            browser.fill("site1NeIpAddress",l[0])
            browser.fill("site1SubnetMask",l[1])
            browser.fill("site1OSPFId",l[2]) 


            #FarEnd
            l1=FarEnd.split("_")
            browser.fill("site2NeIpAddress",l1[0])
            browser.fill("site2SubnetMask",l1[1])
            browser.fill("site2OSPFId",l1[2])
        except AttributeError:
            print "IP NOT UPDATED"
            pass
        
       



