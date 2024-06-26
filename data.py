import pymongo

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://edwardalvin:mBDH6fh9bUjCDcA2@reseearch.a2rwr6l.mongodb.net/?retryWrites=true&w=majority&appName=reseearch"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


db = client["research"]
collection = db["data"] 

intents_data =  [
      {
        "tag": "Greetings",
        "patterns": [
          "Hi",
          "hi",
          "Hey",
          "Hi there!",
          "Is anyone there?",
          "Who are you?",
          "Hello",
          "Yo"
        ],
        "responses": [
          "Hi, welcome to Predoctoral Implant Program. How may I assist you today?",
          "Hello there! Welcome to Predoctoral Implant Program. How may I assist you today?"
        ]
      },
      {
        "tag": "General",
        "patterns": [
            "What is STI?",
            "STI is?",
            "STI",
            "S"
        ],
        "responses": [
          "STI also known as Single Tooth Implant."
         
        ]
      },
      {
        "tag": "STI_Tool_Needed",
        "patterns": ["Which instruments are necessary for treating STI?", 
        "Tools for STI",
        "STI Tools",
        "Can you tell me what instruments are needed to treat STI?", 
        "What kind of tools should I obtain for STI treatment?", 
        "What are the essential instruments for managing STI treatment?",
        "For STI treatment, what instruments should I use?",
        "For STI treatment, what instruments should I secure?",
        "Could you specify the tools required for STI treatment?",
        "What tools are required for effective STI treatment?",
        "Could you list the instruments necessary for STI treatment?",
        "What tools are used for STI?",
        "In terms of STI treatment, what are the necessary instruments?",
        "What instruments are typically used in the treatment of STI?",
        "What tools are used in the treatment of STI?",
        "What are the recommended instruments for STI treatment?",
        "What are the recommended tools for STI treatment?",
        "What is the essential toolkit for STI treatment?",
        "For the treatment of STI, what instruments are required?",
        "What tools are required for STI?",
        "What tools should I prepare for STI treatment?",
        "Can you guide me on the instruments needed for STI treatment?",
        "What equipment is necessary for the treatment of STI?",
        "What tools is necessary for the treatment of STI?",
        "Can you guide me on the instruments needed for STI treatment?",
        "Can you inform me about the instruments required for STI treatment?"


    ],
        "responses": ["You need to get a fixed cassette from the window, x-ray sensor and implant cassette from implant clinic manager office. If the implant is already placed, you need to know which implant system (Brand and size) that your patient has. Please look the patient   s information from the Axium in clinical notes or components used section in forms. If you are taking an impression, you will need to get the implant impression coping and implant analog for conventional PVS impression or Scan body for digital impression."]
      },
      {
        "tag": "STI_Treatment_Codes",
        "patterns": [
          "What is STI Codes?",
          "STI Codes?",
          "What is STI Code",
          "STI Code?",
          "What is the STI Code?",
          "What codes do I have to enter for STI?",
          "Which codes are required for STI?",
          "Can you tell me what codes are needed for STI?",
          "What specific codes should I input for STI?",
          "Could you list the necessary codes for STI?",
          "What are the essential codes for STI?",
          "For STI, what codes should I use?",
          "Could you specify the codes required for STI?",
          "In terms of STI, what are the relevant codes?",
          "What codes should I key in for STI?",
          "Can you guide me on the codes needed for STI?",
          "What are the appropriate codes for STI?",
          "Which codes should I enter when dealing with STI?",
          "Can you inform me about the codes required for STI?",
          "What are the standard codes for STI?",
          "For STI, what are the codes I need to use?",
          "What are the necessary STI codes?",
          "What are the codes I should input for STI?",
          "For STI treatment, what instruments should I secure?",
          "Could you advise on the STI codes to be entered?",
          "Which STI codes should I use?",
          "What STI-related codes do I need to enter?"
        ],
        "responses": [
          " For healed site (tooth that has been extracted): 1. D9365 UG Implant Consultation-STI 2. D0365L CBCT-One arch Mandible or D0366U CBCT-One arch Maxilla (if implants involve two arches, only put one arch code) 3. D6010U2 UG surg. Place. Endosteal implant 4. DD6190 Digital-Radiographic/surgical implant index (only charge one for multiple implants) 5. D6104UG Bone Graft at Impl place (always add no matter apply or not) 6. D7952UG Sinus lift-internal (based on CBCT review, consult with faculty) 7. DD6057 Digital-custom abutment 8. DD6058 Digital-all porcelain/ceramic crown on abutment (cement retained) 9. UG-implant recall-STI # For extracted site (tooth is present that needs to be extracted first): 1. D9365 UG Implant Consultation-STI 2. D7140 Extraction 3. D7953UG Extraction site preservation/graft 4. D0365L CBCT-One arch Mandible or D0366U CBCT-One arch Maxilla (if implants involve two arches, only put one arch code) 5. D6010U2 UG surg. Place. Endosteal implant 6. DD6190 Digital-Radiographic/surgical implant index (only charge one for multiple implants) 7. D6104UG Bone Graft at Implant placement (always add no matter apply or not) 8. D7952UG Sinus lift-internal (based on CBCT review, consult with faculty) 9. DD6057 Digital-custom abutment 10. DD6058 Digital-all porcelain/ceramic crown on abutment (cement retained) 11. UG-implant recall-STI"
        ]
      },
      {
        "tag": "STI_Treatment_Extraction_Approval",
        "patterns": [
            "Who need to approve STI codes?",
            "Who is responsible for approving STI codes?",
            "Can you tell me who should approve the STI codes?",
            "Who has the responsibility for approving codes related to STI?",
            "Who is the approver of the STI codes?",
            "Who should I seek approval from for STI codes?",
            "In terms of STI codes, who is in charge of their approval?",
            "Can you guide me on who should authorize the STI codes?",
            "Whose authorization is required for STI codes?",
            "Who should give the go-ahead for STI codes?",
            "Who holds the authority for the approval of STI codes?",
            "Who is the faculty responsible for approving the STI codes?",
            "Who needs to green-light the STI codes?",
            "Which faculty should approve the STI codes?"
        ],

        "responses": [
          "Your restorative faculty need to approve these codes."
        ]
      },
      {
        "tag": "STI_Appointment_Consultation",
        "patterns": [
            "How long should I wait for an STI consultation after extraction or extraction plus site preservation procedure?",
            "What is the advised waiting duration for an STI consultation following an extraction or extraction plus site preservation procedure?",
            "Following an extraction or extraction plus site preservation procedure, how much time should I allow before scheduling an STI consultation?",
            "Can you specify the appropriate wait time for an STI consultation after undergoing an extraction or extraction plus site preservation procedure?",
            "After having an extraction or extraction plus site preservation procedure, what is the recommended timeframe before consulting about STI?",
            "How long is it typically advised to wait before having an STI consultation following an extraction or extraction plus site preservation procedure?",
            "What's the suggested waiting interval for an STI consultation after an extraction or extraction plus site preservation procedure?",
            "What is the optimal time to wait before seeking an STI consultation after an extraction or extraction plus site preservation procedure?",
            "Can you advise on the typical waiting duration before an STI consultation following an extraction or extraction plus site preservation procedure?",
            "How many days are generally recommended to wait for an STI consultation after an extraction or extraction plus site preservation procedure?"
        ],
        "responses": [
          "You need to wait at least 3 months after tooth extraction and at least 4 months after tooth extraction plus site preservation."
        ]
      },
      {
        "tag": "STI_Treatment_Fee",
        "patterns": [
            "What is the estimated fee for STI treatment when a patient asks me during a UG STI consultation appointment?",
            "What's the projected cost of STI treatment a patient might inquire about during a UG STI consultation appointment?",
            "During a UG STI consultation, what is the expected price range for STI treatment if asked by a patient?",
            "Can you tell me the anticipated cost for STI treatment that might be questioned by a patient during a UG STI consultation appointment?",
            "What could be the approximate fee for STI treatment that a patient may seek during a UG STI consultation appointment?",
            "What is the probable charge for STI treatment a patient might want to know during a UG STI consultation appointment?"
        ],
        "responses": [
          "You can tell the patient that the estimated fee for a single implant including restoration is between $1500 to $1800 (without insurance coverage) depends on what specific procedure is performed."
        ]
      },
      {
        "tag":"STI_Tool_Crown_Action",
        "patterns":[
        
            "I am going to deliver an implant crown, what should I do first?",
            "What should be my initial step when I'm preparing to deliver an implant crown?",
            "Before delivering an implant crown, what is the first action I should take?",
            "When it comes to delivering an implant crown, what should be my first move?",
            "What is the initial procedure I need to follow when delivering an implant crown?",
            "I'm about to deliver an implant crown, what should be my preliminary step?"
        ],
        "responses":[
            "You need to get a fixed cassette from the window, x-ray sensor, implant cassette and torque wrench from the implant clinic manager office. You need to know which implant system that your patient has. Please look the patient   s information from the Axium in clinical notes or components used section in forms. If crown was cement retained, you will need teflon tape available in unit drawer and Panavia cement available in digital lab fridge."

        ]
      },
      {
        "tag":"STI_Tool_Crown_Implant_Steps",
        "patterns":
        [
            "What are the steps to deliver an implant crown?",
            "Could you outline the procedure for delivering an implant crown?",
            "What is the protocol to follow when delivering an implant crown?",
            "Can you describe the process for delivering an implant crown?",
            "What sequence of actions should I follow to deliver an implant crown?",
            "What is the recommended procedure for the delivery of an implant crown?"
        ],
        "responses":[
            "1.Get instruments. 2.Start check with faculty. 3.Evaluate tissue and x-ray. 4.Remove healing abutment. 5.Place custom abutment. 6.Try crown on and adjust the crown interproximal contacts, make sure that the crown is seated all the way down, please take a vertical bitewing to verify full seating. 7.After the crown is seated all the way down, you need to adjust the occlusion using shimstock. 8.Check with faculty for intraoral or extraoral cementation. 9.Let the instructor torque the abutment/crown. Or you need to torque the abutment with the faculty. 10.Fill the screw access hole with teflon and composite. 11.Verify margins, interproximal contacts and occlusion. 12.Polish occlusal/adjusted surface. 13.Give post-op instructions & dismiss patient."
        ]
      },
      {
        "tag":"About_STI_Protocol_Approval",
        "patterns":
        [
            "The implant treatment was approved last year, what do I have to do now?",
            "Given that the implant treatment was approved last year, what is the next step I should take?",
            "Now that the implant treatment was authorized a year ago, what actions should I undertake?",
            "What should I do now, considering the implant treatment was given the green light last year?",
            "Following the approval of the implant treatment last year, what are my current responsibilities?",
            "Given the fact that the implant treatment was sanctioned last year, what procedures should I now follow?"

        ],
        "responses":[
            "Since the treatment was approved last year, you may want to update the medical history and x-ray. Please bring the patient to implant clinic to updates all the information and discuss with faculty."

        ]
      },
      {
        "tag":"About_STI_Crown_Appointment",
        "patterns":
        [
            "How long should I schedule to do crown delivery?",
            "What is the recommended duration for scheduling a crown delivery?",
            "How much time should I allocate for a crown delivery session in my schedule?",
            "What is the typical timeframe for scheduling a crown delivery?",
            "For a crown delivery, how long should the scheduled slot be?",
            "Can you advise on the appropriate length of time to allot for a crown delivery?"
        ],

        "responses":[
            "For crown delivery, you need to schedule for 1 session (3 hours). Please make sure that you have the abutment and crown ready prior to patients appointment"

        ]
      },
      {
        "tag":"About_STI_Protocol_Implant_Consulation",
        "patterns":
        [
            "Is it possible to conduct an implant consultation while the tooth is still in place?",
    "Can an implant consultation be performed with the tooth still present?",
    "Is it permissible to carry out an implant consult when the tooth remains?",
    "Can I proceed with an implant consultation even though the tooth has not been removed?",
    "Is conducting an implant consult feasible while the tooth is still intact?"
            
        ],

        "responses":[
            "Yes, you can do implant when the tooth still there for anterior and premolar sites. For molar sites, consult should be done 2 months post extraction. Please discuss with implant faculty."
        ]
        
      },
      {
        "tag":"About_STI_Protocol_Tooth89",
        "patterns":
        [
            "Can I do consult for number 8 and 9?",
    "Is it feasible to conduct a consultation for 8 and 9?",
    "Can I perform a consult for # 8 and # 9?",
    "Is a consultation for tooth number 8 and 9 a possibility?",
    "Can a consult be arranged for # 8 and # 9?",
    "Is it permissible to carry out a consult for tooth number 8 and 9?"
        ],

        "responses":[
            "Predoctoral implant clinic does not accept STI treatment to replace teeth #8, 9. Please refer the case to Post Graduate Prosthodontics for further treatment."
        ]
        
      },
      {
        "tag":"About_STI_Protocol_Second_Molar",
        "patterns":
        [
            "Can I do consult for second molar?",
            "Is it feasible to conduct a consultation for second molar?",
            "Can I perform a consult for second molar?",
            "Is a consultation for the second molar a possibility?",
            "Can a consult be arranged for the tooth referred to as second molar?",
            "Is it permissible to carry out a consult for second molar?"
        ],

        "responses":[
            "We typically do not do implant tx for second molar, however, if you think the case is ideal, please consult with implant faculty."
        ]
      },
      {
        "tag":"About_STI_Protocol_Implant_Bridge",
        "patterns":
        [
            "Can we treat implant-supported bridge?",
            "Is it feasible to provide treatment for implant-supported bridge?",
            "Can our practice administer care for implant-supported bridge?",
            "Is the treatment of an implant-supported bridge within our scope of services?",
            "Do we have the capacity to manage care for an implant-supported bridge?",
            "Can our facility handle treatment protocols for implant-supported bridge?"
        ],

        "responses":[
            "Predoctoral implant clinic does accept implant supported bridge treatment for posterior teeth only. Please make a consult in the implant clinic."

        ]
        
      },
      {
        "tag":"About_STI_Protocol_Implant_Number",
        "patterns":
        [
            "What is the maximum number of implants for one patient that can be accepted for UG implant program?",
            "Whats maximum implant i can restore?",
            "Whats the maximum impant can be restored?",
            "What is the upper limit of implants a single patient can have under the UG implant program?",
            "Under the UG implant program, what is the maximum quantity of implants one patient can receive?",
            "What's the cap on the number of implants a patient can be provided with in the UG implant program?",
            "What is the highest number of implants a patient can be approved for under the UG implant program?",
            "In the UG implant program, what's the most implants a single patient can have?"
            
        ],

        "responses":[
            "The maximum number of implants for one patient is 4 implants."
        ]
        
      },
      {
        "tag":"STI_Appointment_Final_Impression",
        "patterns":
        [
            "How long should I wait for implant final impression after uncovery implant procedure?",
            "What is the recommended waiting period for an implant final impression following an implant uncovery procedure?",
            "After performing an implant uncovery procedure, how long should I wait before taking the final implant impression?",
            "What's the appropriate time interval between the implant uncovery procedure and taking the final implant impression?",
            "How much time should elapse after an implant uncovery procedure before proceeding with the final implant impression?",
            "Following the uncovery of an implant, what is the advised wait time before obtaining the final implant impression?"
        ],

        "responses":[
            "You need to wait at least 2 weeks to take implant final impression after uncovery implant procedure."
        ]
        
      },
      {
        "tag":"About_STI_Protocol_Implant_Restoration",
        "patterns":
        [
            "Can I restore the implant that was placed outside UIC COD?",
            "Is it possible to restore an implant that was placed outside of UIC COD?",
            "Can an implant placed outside the UIC COD be subjected to restoration?",
            "Am I allowed to carry out a restoration on an implant that was placed beyond UIC COD?",
            "Is it permissible to restore an implant that was implanted outside UIC COD?",
            "Can I undertake a restoration process on an implant that was installed outside of UIC COD?"
        ],

        "responses":[
            "We do not typically restore implant that was placed outside UIC COD. However, if the implants are either Straumann or Astra Dentsply, you may want to discuss the case with implant faculty."
        ]
        
      },
      {
        "tag":"About_STI_Protocol_Extraction_Site",
        "patterns":
        [
            "Can I do extraction and site preservation procedure?",
            "Is it feasible for me to perform an extraction and site preservation procedure?",
            "Am I capable of carrying out extraction and site preservation procedure?",
            "Is it permissible for me to conduct a tooth extraction along with a site preservation procedure?",
            "Can I undertake both an extraction and site preservation procedure?",
            "Is it within my capabilities to perform a tooth extraction in conjunction with a site preservation procedure?" 
        ],

        "responses":[
            "You can talk with UG OS department director Dr. William Flick, if it   s not complex extraction, they will let you do the procedure in UG OS department."
        ]
        
      },
      {
        "tag":"About_STI_Protocol_Screwretained_Implant",
        "patterns":
        [
            "Can I do screw-retained implant restoration?",
            "Is it feasible for me to perform a screw-retained implant restoration?",
            "Am I capable of carrying out a screw-retained implant restoration procedure?",
            "Is it permissible for me to conduct a screw-retained implant restoration?",
            "Can I undertake a screw-retained implant restoration?",
            "Is it within my capabilities to perform a screw-retained implant restoration?"
            
        ],

        "responses":[
            "Yes, you can do screw-retained implant restoration. Please discuss with implant faculty if you want to do so."
        ]
        
      },
      {
        "tag":"About_STI_Protocol_Wax_Cast",
        "patterns":
        [
            "Can I do implant STI consult without wax-up or cast?",
            "Is it feasible to conduct an implant STI consultation without a wax-up or cast?",
            "Can an implant STI consult be performed in the absence of a wax-up or cast?",
            "Is it permissible to carry out an implant STI consult without using a wax-up or cast?",
            "Can I proceed with an implant STI consult without the need for a wax-up or cast?",
            "Is conducting an implant STI consult feasible without the use of a wax-up or cast?"
        ],

        "responses":[
            "We highly recommend having diagnostic wax-up on the cast for implant STI consult."
        ]
      },
      {
        "tag":"STI_Appointment_STI_Consultation",
        "patterns":
        [
            "How long should I schedule the appointment for STI consultation?",
            "What is the recommended duration for scheduling an STI consultation appointment?",
            "How much time should I allocate for an STI consultation session in my schedule?",
            "What is the typical timeframe for scheduling an STI consultation appointment?",
            "For an STI consultation, how long should the scheduled slot be?",
            "Can you advise on the appropriate length of time to allot for an STI consultation appointment?"
        ],

        "responses":[
            "You can schedule 1.5 hours for STI consultation."
        ]
        
      },
      {
        "tag":"About_STI_Protocol_Consultation",
        "patterns":
        [
            "Can I do STI consult if the patient is still undergoing orthodontic treatment?",
    "Is it feasible to conduct an STI consultation while the patient is still undergoing orthodontic treatment?",
    "Can an STI consult be performed if the patient is currently engaged in orthodontic therapy?",
    "Is it permissible to carry out an STI consult when the patient is still in the midst of orthodontic treatment?",
    "Can I proceed with an STI consult even though the patient is not yet finished with orthodontic care?",
    "Is conducting an STI consult feasible while the patient is still receiving orthodontic treatment?",
    "Can I do STI consult if the patient is going to have an orthodontic consult or treatment?",
    "Is it feasible to conduct an STI consultation if the patient is due to have an orthodontic consultation or treatment?",
    "Can an STI consult be performed if the patient is about to engage in orthodontic therapy or consultation?",
    "Is it permissible to carry out an STI consult when the patient is set to begin orthodontic treatment or consultation?",
    "Can I proceed with an STI consult even if the patient is on the verge of having an orthodontic consult or treatment?",
    "Is conducting an STI consult feasible if the patient is preparing for an orthodontic consultation or treatment?"
        ],

        "responses":[
            "No, it is advisable to wait until the completion of the orthodontic treatment."
        ]
        
      },
      {
        "tag":"STI_Treatment_Plan_Home_Clinic",
        "patterns":
        [
            "Can I ask for STI consult when my patient is being treated in my home clinic that may need an implant?",
            "Is it possible to request an STI consultation if my patient, currently being treated in my home clinic, may require an implant?",
            "Can I seek an STI consult when my patient, receiving treatment in my home clinic, might need an implant?",
            "Is it permissible to call for an STI consult for my patient in my home clinic, who may necessitate an implant?",
            "Can I initiate an STI consult if my patient, undergoing treatment in my home clinic, could potentially require an implant?",
            "Is it feasible to arrange an STI consultation for my patient in my home clinic, who might be in need of an implant?"
        ],

        "responses":[
            "First, ask implant clinic faculty for permission and double check If there is a chair available. Upon faculty approval, request Fabi to add your patient   s name in the schedule, and then you can bring your patient to Chicago implant clinic for STI consult."
        ]
      },
      {
        "tag":"STI_Tool_Abutment_Process",
        "patterns":
        [
            "How do I evaluate the abutment during the abutment try-in appointment?",
    "What is the process for evaluating the abutment during the abutment try-in appointment?",
    "Can you guide me on how to assess the abutment in the course of the abutment try-in appointment?",
    "What steps should I follow to evaluate the abutment during the abutment try-in session?",
    "How should I go about assessing the abutment at the time of the abutment try-in appointment?",
    "What approach should I take to evaluate the abutment during the abutment try-in appointment?" 
        ],

        "responses":[
            "1.Digital image: Faculty will access the Atlantis Weborder to review the digital design of custom abutment. This design will serve as a reference during the abutment try-in. 2.Fit: The primary concern is to make sure the abutment fits correctly on the implant. Screw the abutment into the implant to check the fit and verified with x-ray. It should seat completely without any gaps. Also, check for any movement or rocking when it is seated. 3.Margin Integrity: Use a periodontal probe to assess the integrity of the abutment margins. Margins should not impinge on soft tissues and ideally, they should be slightly supragingival on lingual/palatal side and slightly subgingival on buccal side to facilitate oral hygiene and esthetics. 4.Restorative space: Evaluate mesial, distal and occlusal space to the adjacent and opposing teeth, allowing sufficient restorative space for E.max crown (at least 2 mm interocclusal space). 5.Soft Tissue Health: Look for any signs of soft tissue inflammation or irritation. Remember that patient comfort and feedback are also important. Ask the patient if they feel any discomfort during this try-in stage. The abutment should not cause any discomfort to the patient that lasts more than 15 mins, unless the healing abutment is significantly smaller than the custom abutment. Any concerns raised by the patient should be addressed before proceeding with the final prosthetic stage."
        ] 
      },
      {
        "tag":"STI_Material_Cementation",
        "patterns":
        [
            "What cement do I use for implant crown cementation?",
            "Which type of cement should be employed for implant crown cementation?",
            "What kind of cement is appropriate to use during the cementation of an implant crown?",
            "Can you advise on the cement to be used for implant crown cementation?",
            "What is the preferred cement for cementation of an implant crown?",
            "Which cement is typically used for the cementation process of an implant crown?"
        ],

        "responses":[
            "You need to get Panavia (resin cement) from the fridge in the digital lab."
        ]
        
      },
      {
        "tag":"STI_Appointment_Followup_Crown",
        "patterns":
        [
            "How long should I wait to schedule for the first follow-up appointment after implant crown delivery?",
    "What is the recommended waiting period before scheduling the first follow-up appointment post implant crown delivery?",
    "How much time should elapse before arranging the first follow-up visit after delivering an implant crown?",
    "After implant crown delivery, how long should I wait before scheduling the initial follow-up appointment?",
    "What's the typical waiting period to schedule the first follow-up consultation following implant crown delivery?",
    "Can you advise on the suitable duration to wait before setting up the first follow-up appointment after implant crown delivery?"
        ],

        "responses":[
            "You should schedule a 1-week follow-up appointment after implant crown delivery."
        ]
        
      },
      {
        "tag":"About_STI_Protocol_Radiographic",
        "patterns":
        [
            "For the radiographic guide, if it's one tooth, do I need to make the full arch?",
            "In the case of a single tooth, is it necessary to create a full-arch radiographic guide?",
            "Do I need to construct a full-arch radiographic guide even if it's only for one tooth?",
            "For a radiographic guide, if I'm focusing on a single tooth, is a full arch required?",
            "When creating a radiographic guide for a single tooth, should I still make a full arch?",
            "If it's just for one tooth, is a full arch necessary when developing a radiographic guide?"
        ],

        "responses":[
            "No, you do not need to make a full arch radiographic guide for one tooth."
        ]
        
      },
      {
        "tag":"STI_Treatment_Plan_Digital_Impression",
        "patterns":
        [
            "Can I do a digital implant impression if it is my first implant impression?",
            "Is it feasible to perform a digital implant impression if this is my first time doing an implant impression?",
            "Can I carry out a digital impression for an implant even if it's my initial experience with implant impressions?",
            "Is it permissible to undertake a digital implant impression for my very first implant impression procedure?",
            "For my first implant impression, can I opt for a digital approach?",
            "Even if it's my first time doing an implant impression, can I utilize digital impression techniques?"
            
        ],

        "responses":[
            "It is strongly advised to begin your first implant impression using the conventional technique, as this allows you to grasp the fundamental principles. For your second implant impression, you can then incorporate digital implant impression technology."
        ]
        
      },
      {
        "tag":"STI_Tool_Digital_Impression_Steps",
        "patterns":
        [
            "I am planning to do STI digital impression. What are the steps that I need to do?",
    "What procedures should I follow if I intend to perform a digital impression for STI?",
    "Can you guide me on the steps required for performing a digital impression for STI?",
    "What are the necessary steps to execute a digital impression for STI if I am planning to do so?",
    "In planning for an STI digital impression, what procedures do I need to adhere to?",
    "If I aim to conduct a digital impression for STI, what are the steps I need to undertake?" 
        ],

        "responses":[
            "1.Check the implant brand and diameter. 2.Start check with faculty. 3.Fabi for corresponding Scanbody. 4.Get intraoral scanner from digital lab. 5.Remove healing abutment and scan the same arch. 6.Insert Scanbody, make sure it   s fully seated and confirm with x-ray. 7.Scan the Scanbody (you don   t need to scan the whole arch, just the implant site). 8.Scan the opposing arch and scan the bite. 9.Click    post-processing    and send to    UIC Lab   . 10.Get the shade. 11.Double check with faculty and dismiss the patient. 12.Clean instruments and return the intraoral scanner."
        ]
        
      },
      {
        "tag":"STI_Tool_Phase",
        "patterns":
        [
            "Can I do implant STI consult if Phase 1 treatment is not completed?",
            "Is it possible to conduct an implant STI consultation if the patient hasn't completed Phase 1 treatment?",
            "Can an STI consultation for an implant be performed even if Phase 1 treatment isn't finished?",
            "Is it permissible to execute an implant STI consult while Phase 1 treatment remains incomplete?",
            "Can I proceed with an implant STI consultation if the patient is still in the midst of Phase 1 treatment?",
            "Is it feasible to conduct an STI consultation for an implant if Phase 1 treatment isn't fully completed?"
        ],

        "responses":[
            "All phase 1 treatments must be completed before forwarding patient to PG resident for implant placement."
        ]
        
      },
      {
        "tag":"STI_Treatment_UG",
        "patterns":
        [
            "Can I accept a patient for UG STI that needs lateral approach maxillary sinus augmentation?",
            "Is it permissible to admit a patient for UG STI if they require a lateral approach maxillary sinus augmentation?",
            "Can a patient requiring lateral approach maxillary sinus augmentation be accepted into the UG STI program?",
            "Is it possible to accept a patient for the UG STI program if they need a lateral approach to maxillary sinus augmentation?",
            "Can I enroll a patient in UG STI who necessitates a lateral approach for maxillary sinus augmentation?",
            "If a patient needs a lateral approach for maxillary sinus augmentation, is it feasible to include them in the UG STI?"
            
        ],

        "responses":[
            "We do not accept patient who requires lateral approach sinus augmentation as the process may significantly prolong the time required for the patient's return to the UG student for implant restoration."
        ]
        
      },
      {
        "tag":"STI_Treatment_Boneloss",
        "patterns":
        [
            "Can I restore an implant that has marginal bone loss?",
            "Is it feasible to restore an implant that presents with marginal bone loss?",
            "Can a restoration be performed on an implant associated with marginal bone loss?",
            "Is restoration possible for an implant that is showing signs of marginal bone loss?",
            "Can I perform a restoration procedure on an implant that has experienced marginal bone loss?",
            "Is it permissible to restore an implant that has been affected by marginal bone loss?"
        ],

        "responses":[
            "Please have a discussion with your implant faculty regarding this issue."
        ]
        
      },
      {
        "tag":"STI_Material_Tray_Impression",
        "patterns":
        [
            "How can I select closed-tray or open-tray impression technique?",
            "What factors should I consider when deciding between closed-tray and open-tray impression techniques?",
            "How do I determine whether to use a closed-tray or open-tray impression technique?",
            "What are the advantages and disadvantages of the closed-tray and open-tray impression techniques?",
            "What clinical indications would lead me to choose a closed-tray impression technique over an open-tray technique, or vice versa?",
            "Can you explain the decision-making process for selecting between closed-tray and open-tray impression techniques in dental procedures?"
        ],

        "responses":[
            "The choice between closed-tray and open-tray impression techniques should be based on a comprehensive evaluation of the clinical situation, patient factors, and your own expertise. Consulting with your faculty for selecting the specific impression technique."
        ]
        
      },
      {
        "tag":"STI_Treatment_Immediate_Implant_Placement",
        "patterns":
        [
            "Can I accept a patient for immediate implant placement?",
    "What criteria should be considered when determining if a patient is suitable for immediate implant placement?",
    "Are there specific conditions or factors that would make a patient a good candidate for immediate implant placement?",
    "What are the key considerations in deciding whether a patient is appropriate for immediate implant placement?",
    "How can I assess a patient's eligibility for immediate implant placement?",
    "What are the potential risks and benefits associated with accepting a patient for immediate implant placement?"
        ],

        "responses":[
            "Please discuss with your faculty if certain criteria are met, such as adequate bone quantity and quality, good primary stability of the implant, absence of infection or active periodontal disease, and patient's overall health status. A comprehensive evaluation is necessary to determine if immediate implant placement is suitable for the individual patient."
        ]
        
      },
      {
        "tag":"STI_Treatment_Immediate_Implant_Placement_ToothNumber",
        "patterns":

        [
            "Which tooth number is acceptable for immediate implant placement?",
            "Are there specific criteria or guidelines for determining the suitability of a tooth number for immediate implant placement?",
            "What factors should be taken into consideration when deciding on the tooth number for immediate implant placement?",
            "How can I determine if a particular tooth number is appropriate for immediate implant placement?",
            "Are there any limitations or restrictions on which tooth number can receive immediate implant placement?",
            "What are the general considerations when selecting a tooth number for immediate implant placement?"
        ],

        "responses":[
           "Please consult with your faculty to determine if the specific criteria are met. We we do not accept molar immediate implant "
    
        ]
        
      },
      {
        "tag":"About_STI_Protocol_Guide",
        "patterns":
        [
            "Do I need to make a surgical/radiographic guide if the tooth is accepted for immediate implant placement?",
            "Is it necessary to create a surgical or radiographic guide when performing immediate implant placement?",
            "What are the advantages and disadvantages of using a surgical or radiographic guide for immediate implant placement?",
            "How does the use of a surgical or radiographic guide impact the success and accuracy of immediate implant placement?",
            "Are there specific cases or situations where the creation of a surgical or radiographic guide is highly recommended for immediate implant placement?",
            "What are the considerations and factors that should be weighed when deciding whether or not to utilize a surgical or radiographic guide during immediate implant placement?"
        ],

        "responses":[
            "If the tooth is still present, you do not need to make surgical or radiographic guide."
        ]
        
      },
      {
        "tag":"About_STI_Extraction_Site_Preservation",
        "patterns":
        [
            "If my patient had the extraction done as well as site preservation, what do I need to do next?",
    "After performing tooth extraction and site preservation for my patient, what are the next steps in the treatment process?",
    "What is the recommended course of action following a procedure involving tooth extraction and site preservation for a patient?",
    "What additional measures or procedures should be taken after completing tooth extraction and site preservation for a patient?",
    "Can you outline the post-operative care and follow-up requirements for a patient who has undergone tooth extraction and site preservation?",
    "In cases where tooth extraction and site preservation has been performed, what are the subsequent treatment considerations and protocols that need to be followed?" 
        ],

        "responses":[
            "Schedule the patient back in Chicago implant clinic for STI consult at least 3 months after the extraction and site preservation"
        ]
        
      },
      {
        "tag":"STI_Tool_Implant_System",
        "patterns":
        [
            "How do I know what implant system my patient was assigned to?",
    "What steps should I take to determine the implant system that has been assigned to my patient?",
    "Are there specific records or documentation that can help me identify the implant system assigned to my patient?",
    "How can I retrieve information about the implant system used for my patient's treatment?",
    "Are there any visual or physical indicators that can assist me in identifying the implant system my patient has been assigned to?",
    "What resources or sources of information should I consult to ascertain the implant system assigned to my patient?"

        ],

        "responses":[
            "Check Axium note for surgical implant placement or Axium components used form. It is crucial not just to know the implant system, but also to be aware of the implant diameter. This information is vital for selecting impression coping for final impression and lab script for custom abutment fabrication."
        ]
        
      },
      {
        "tag":"STI_Tool_Abutment_Prescription",
        "patterns":
        [
            "What do I have to write down for abutment prescription?",
            "What information should be included in the abutment lab script?",
            "Can you provide a list of essential details that need to be documented in the abutment prescription or lab script?",
            "What specific instructions or specifications should be noted in the abutment prescription for accurate fabrication?",
            "Are there any particular measurements or parameters that need to be recorded in the abutment prescription?",
            "What are the necessary guidelines or requirements for documenting the abutment type and characteristics in the abutment prescription?" 
        ],

        "responses":[
            "You need to write down the following: Please fabricate atlantis abutment for implant #. Type of implant, Straumann/Dentsply, Diameter X. Abutment type: Titanium for posterior teeth/Gold hue for anterior teeth. Emergence profile: default."
        ]
        
      },
      {
        "tag":"STI_Tool_Crown_Prescription",
        "patterns":
        [
            "What do I have to write down for crown prescription?",
            "When prescribing a dental crown, what specific information should be included in the lab script to ensure accurate fabrication?",
            "What are the key details that need to be documented in the crown prescription for successful crown production?",
            "Can you guide me on the necessary instructions and specifications that should be written in the crown prescription?",
            "Are there any specific measurements or parameters that I need to provide in the crown prescription?",
            "What guidelines or requirements should I follow when documenting the desired crown material, shade, and other relevant information in the crown prescription?"
        ],

        "responses":[
            "You need to write down the following: Please fabricate emax crown for implant #. Final prosthesis: cement retained crown. Shade XX"
        ]
        
      },
      {
        "tag":"STI_Tool_Screw_Retained_Crown_Prescription",
        "patterns":
        [
            "What do I have to write down for screw retained crown prescription?",
    "When prescribing a screw-retained crown, what specific information should be included in the prescription to ensure accurate fabrication?",
    "Can you provide a comprehensive list of details that need to be documented in the screw-retained crown prescription?",
    "What specific instructions or specifications should be noted in the screw-retained crown prescription for precise manufacturing?",
    "Are there any particular measurements or parameters that need to be recorded in the screw-retained crown prescription?",
    "What guidelines or requirements should I follow when documenting the desired crown material, implant system compatibility, and other relevant information in the screw-retained crown prescription?" 
        ],

        "responses":[
            "You need to write down the following: Please fabricate screw retained PFM for implant #. Type of implant, Straumann/Dentsply, Diameter X. Enclosed you will find the UCLA abutment. Shade: XX"
        ]
        
      },
      {
        "tag":"About_STI_Protocol_Custom_Abutment",
        "patterns":
        [
            "Can I try-in the custom abutment and deliver the implant crown in one session?",
            "Is it possible to perform a try-in of the custom abutment and deliver the implant crown in a single session?",
            "Can you provide guidance on whether it is feasible to conduct both the try-in of the custom abutment and the delivery of the implant crown during one appointment?",
            "Are there any specific considerations or factors that may influence the decision to combine the try-in of the custom abutment and the delivery of the implant crown into a single session?",
            "Is it within the treatment protocol to perform the try-in of the custom abutment and the delivery of the implant crown concurrently during a single appointment?",
            "Can you explain the advantages, challenges, and potential outcomes associated with conducting the try-in of the custom abutment and delivering the implant crown in one session?" 
        ],

        "responses":[
            "The recommended protocol is to schedule the patient for the custom abutment try-in prior to the crown fabrication. However, you can discuss with the implant faculty the possibility of doing so in case there were time limitation or inconvenience issues."
        ]
        
      },
      {
        "tag":"IOD_Tool_Treatment",
        "patterns":
        [
            "What instruments do I need to get for IOD treatment?",
            "What tools do I need for IOD treatment?",
            "What instruments for IOD?",
            "What tools should I have for IOD treatment",
            "What should I have for IOD Treatment?",
            "Which specific dental instruments and tools are essential for performing an IOD treatment?",
            "Can you provide a comprehensive list of instruments and equipment required for IOD treatment?",
            "What are the necessary dental instruments and tools that should be prepared in advance for a successful IOD procedure?",
            "Are there any specialized instruments or devices that are recommended for use during IOD treatment?",
            "Could you guide me on the specific dental instruments I should acquire or have readily available for an IOD procedure?"
        ],

        "responses":[
            "You need to get a fixed cassette from the window, xray sensor and implant cassette from the window. You need to know which implant system that you the patient has. Please look the patient   s information from the axium."
        ]
        
      },
      {
        "tag": "IOD_Protocol_Treatment_Codes",
        "patterns": [
            "What codes do I have to enter for IOD?",
            "What is the treatment code for IOD?",
            "IOD Codes",
            "What is the IOD Code?",
            "Are there specific billing or procedure codes that need to be entered when documenting an IOD treatment?",
            "Can you provide guidance on the necessary coding requirements for accurately documenting an IOD procedure?",
            "What are the recommended codes that should be entered in the billing system for proper identification of an IOD treatment?"
        ],
        "responses": [
            "Faculty:\n1. D9360 UG Implant Consultation-IOD\n2. D0365L CBCT-One arch Mandible or D0366U CBCT-One arch Maxilla (if implants involve two arches, only put one arch code)\n3. DD6190 Digital-Radiographic/Surgical Implant Index\n4. D7321 Alveoloplasty W/O Ext., 1-3 Spaces/Quads (always add this code no matter apply or not) X2\n5. D6010U1 UG-OD (Overdenture), Surgical Placement x2\n6. D6056U1 UG-OD (Overdenture), Prefab. Abutment x2\n7. D5875 Modification of Removable Prosthesis\n8. D0106 UG Implant Recall Exam-OD"
        ]
    },
    
      {
        "tag":"About_IOD_Protocol_Approval",
        "patterns":
        [
            "Who needs to approve IOD codes?",
            "In the process of documenting an IOD treatment, who is responsible for approving the assigned codes?",
            "Which individuals or entities have the authority to review and approve the IOD codes before they are finalized?",
            "Are there specific personnel or departments that need to verify and authorize the IOD codes before submission?"    
        ],

        "responses":[
            "Your restorative faculty need to approve these codes."
        ]
        
      },
      {
        "tag":"IOD_Treatment_Fee",
        "patterns":
        [
            "What is the estimated fee for IOD treatment when a patient asks me during UG IOD consultation appointment?",
            "When a patient asks about the cost of an IOD treatment during an undergraduate IOD consultation appointment, what information should be provided regarding the estimated fee?",
            "Can you provide an approximate cost estimate for an IOD treatment when discussing it with a patient during a UG (Undergraduate) IOD consultation appointment?",
            "What factors should be considered when providing an estimated fee for an IOD treatment during a consultation appointment with an undergraduate patient?",
            "Are there any additional charges or variables that may impact the estimated fee for an IOD treatment, and how can they be conveyed to the patient during a UG IOD consultation?",
            "How can the estimated fee for an IOD treatment be effectively communicated to a patient during a UG IOD consultation appointment, taking into account potential variations based on individual circumstances?"
        ],

        "responses":[
            "You can tell the patient that the estimated fee for two implant placement plus overdenture conversion is between $875 to $1300 (without insurance coverage) depends on what specific procedure is"
        ]
        
      },
      {
        "tag":"IOD_Appointment_Pickup",
        "patterns":
        [
            "How long should I schedule to do IOD pick up?",
            "What is the recommended duration that should be allocated for performing the IOD pick-up procedure?",
            "Can you provide guidance on the appropriate time frame for scheduling and conducting the IOD pick-up process?",
            "How much time should be allotted in the schedule to ensure sufficient time for completing the IOD pick-up procedure accurately?",
            "Are there any specific considerations or factors that may influence the length of time needed for the IOD pick-up, and how should they be accounted for in scheduling?",
            "In order to allow for a successful and thorough IOD pick-up, what is the suggested timeframe that should be reserved to perform the procedure effectively?",
            "How long should I schedule to do IOD duplication?"
        ],

        "responses":[
            "For IOD pick up appointment, you need to schedule for 1 session (3 hours)."
        ]
        
      },
      {
        "tag":"IOD_Appointment_Duplication",
        "patterns":
        [
            "How long should I schedule to do IOD duplication?",
            "What is the recommended duration for scheduling and performing the duplication process of an IOD treatment?",
            "Can you provide guidance on the appropriate time frame required for duplicating an IOD accurately and efficiently?",
            "How much time should be allocated in the schedule to ensure a successful duplication of the IOD treatment?",
            "Are there any specific considerations or factors that may influence the length of time needed for IOD duplication, and how should they be accounted for in scheduling?",
            "In order to allow for a thorough and precise duplication of the IOD, what is the suggested timeframe that should be reserved for the duplication process?"
        ],

        "responses":[
            "For IOD duplication, you need to schedule for 1 session (3 hours)."
        ]
        
      },
      {
        "tag":"IOD_Treatment_Maxilla",
        "patterns":
        [
            "Can we do IOD for maxilla?",
            "Is it possible to perform an IOD treatment for the maxilla (upper jaw)?",
            "Are there any limitations or considerations when considering IOD treatment specifically for the maxilla?",
            "Can the IOD technique be applied successfully to the maxillary arch, and are there any specific factors that need to be taken into account?",
            "Is IOD a suitable treatment option for patients who require restoration or implant placement in the upper jaw?",
            "Are there any particular challenges or modifications when performing IOD for the maxilla, and how can they be addressed effectively?"
        ],

        "responses":[
            "Predoctoral implant clinic does not accept IOD treatment for maxilla. Please refer the case to Post Graduate Prosthodontics for further treatment."
        ]
        
      },
      {
        "tag":"IOD_Treatment_Multiple_Implants",
        "patterns":
        [
            "Can we place more than 2 implants for IOD mandible?",
            "Is it feasible to insert more than two implants for an IOD treatment in the mandible (lower jaw)?",
            "Are there any limitations or guidelines on the number of implants that can be placed for IOD in the mandibular arch?",
            "Can the IOD technique accommodate the placement of multiple implants in the mandible?",
            "Is it possible to achieve successful immediate loading with more than two implants in the mandibular region using the IOD approach?",
            "Are there any specific considerations or modifications when placing multiple implants for IOD in the mandible, and how can they be addressed effectively?"
        ],

        "responses":[
            "Predoctoral implant clinic does not accept IOD mandible treatment with more than 2 implants. Please refer the case to Post Graduate Prosthodontics for further treatment."
        ]
        
      },
      {
        "tag":"IOD_Material_Chairside",
        "patterns":
        [
            "What dental material do I use for IOD chairside pick-up?",
            "Which specific dental materials are recommended for chairside pick-up during an IOD procedure?",
            "Can you provide guidance on the appropriate dental material to be used for chairside pick-up in the context of an IOD treatment?",
            "What are the preferred dental materials for chairside pick-up when implementing the IOD technique?",
            "Are there any specific considerations or factors that should influence the choice of dental material for chairside pick-up during IOD, and how should they be taken into account?",
            "In order to ensure a successful chairside pick-up during IOD, which dental material is suggested to be used for optimal results?"
        ],

        "responses":[
            "Self-curing repair acrylic resin is recommended for IOD chairside pick-up due to its high strength property."
        ]
        
      },
      {
        "tag":"IOD_Appointment_Followup_Crown",
        "patterns":
        [
            "How long should I wait to schedule for the first follow-up appointment after IOD delivery?",
            "What is the recommended waiting period before scheduling the first follow-up appointment after the delivery of an IOD treatment?",
            "Can you provide guidance on the appropriate timeframe that should elapse before scheduling the initial post-IOD delivery follow-up appointment?",
            "How much time should pass after IOD delivery to allow for proper healing and stability before scheduling the first follow-up visit?",
            "Are there any specific factors or considerations that may influence the waiting period for scheduling the first follow-up appointment after IOD delivery, and how should they be taken into account?",
            "In order to ensure sufficient time for successful healing and integration, what is the suggested duration that should be observed before scheduling the first post-IOD delivery follow-up appointment?"
        ],

        "responses":[
            "You should schedule a 1-week follow-up appointment after IOD delivery."
        ]
        
      },
      {
        "tag":"IOD_Appointment_Schedule",
        "patterns":
        [
            "How long should I schedule the appointment for STI CBCT?",
            "What is the recommended duration for scheduling an appointment to perform a STI CBCT (Cone Beam Computed Tomography) scan?",
            "Can you provide guidance on the appropriate time frame that should be allocated for a STI CBCT appointment?",
            "How much time should be reserved in the schedule to ensure a thorough and accurate STI CBCT imaging procedure?",
            "Are there any specific considerations or factors that may influence the length of time needed for a STI CBCT appointment, and how should they be taken into account?",
            "In order to allow for comprehensive imaging and analysis, what is the suggested duration that should be scheduled for a STI CBCT scan?"
        ],

        "responses":[
            "You can schedule 1.5 hours for STI CBCT. Please have your radiographic/surgical guide ready prior to the appointment."
        ]
        
      },
      {
        "tag":"IOD_Appointment_Consultation_CD_Delivery",
        "patterns":
        [
            "How long should I wait for IOD consult after CD delivery?",
            "What is the recommended waiting period before scheduling an IOD consultation after the delivery of a CD?",
            "Can you provide guidance on the appropriate timeframe that should elapse before scheduling an IOD consult following the CD delivery?",
            "How much time should pass after the CD delivery to allow for proper adaptation and healing before scheduling the IOD consultation?",
            "Are there any specific factors or considerations that may influence the waiting period for scheduling the IOD consultation after CD delivery, and how should they be taken into account?",
            "In order to ensure adequate time for the patient to acclimate to the crown and for any necessary adjustments, what is the suggested duration that should be observed before scheduling the IOD consult following the CD delivery?"  
        ],

        "responses":[
            "You can do IOD consult as long as the patient does not encounter any problems or requires additional adjustments for at least one follow-up. Please discuss with implant faculty if the CD is ready for IOD."
        ]
        
      },
      {
        "tag":"IOD_Protocol_Observation",
        "patterns":
        [
            "Can I observe or assist PG resident implant surgery?",
            "Is it permissible for me to observe or assist implant surgery performed by a PG (Postgraduate) resident?",
            "Can I participate in or observe implant surgery conducted by a PG resident as part of my learning experience?",
            "Are there any restrictions or guidelines regarding my involvement in implant surgery performed by PG residents?",
            "Is it allowed for me to assist a PG resident during implant surgery to enhance my understanding and skill development?",
            "Can I be present in the operating room and observe the entire process of implant surgery performed by PG residents for educational purposes?"   
        ],

        "responses":[
            "Yes, you can observe or assist PG resident implant surgery. Please email Miss Clarke <clarkes@uic.edu> regarding this matter."
        ]
        
      },
      {
        "tag":"IOD_Protocol_LabScript",
        "patterns":
        [
            "Should I obtain the lab script approval from the same faculty member who oversaw the final impression appointment?",
            "When seeking lab script approval, should I obtain it from the same faculty member who supervised the final impression appointment?",
            "Are there any specific guidelines or recommendations regarding obtaining lab script approval, specifically in relation to the faculty member who supervised the final impression appointment?",
            "Is it necessary or advisable to obtain lab script approval from the same faculty member who was involved in overseeing the final impression appointment?",
            "What is the general protocol or best practice for obtaining lab script approval, and should it be sought from the faculty member who supervised the final impression appointment?"
        ],

        "responses":[
            "We recommend getting the lab approval signature from the same faculty who supervised your implant final impression appointment. However, if that faculty is unavailable or not present at school, you may seek signature from any other implant clinic faculty."
        ]
        
      },
      {
        "tag":"IOD_Protocol_Torque",
        "patterns":
        [
            "When can i use torque?",
            "Torque Wrench",
            "Can I use torque wrench?",
            "Is it permissible for me to utilize a torque wrench during dental procedures?",
            "Can I incorporate the use of a torque wrench as part of my treatment protocol?",
            "Are there any specific guidelines or restrictions regarding the use of a torque wrench in dental practice?"
        ],

        "responses":[
            "Only final implant crown delivery or IOD conversion procedure necessitates the use of a torque wrench. The final torque with torque wrench should be performed exclusively by your instructor."
        ]
        
      },
      {
        "tag":"IOD_Treatment_Fee_Radiographic",
        "patterns":
        [
            "If the patient already paid for the regular radiographic guide, do they need to pay for the Digital one too?",
            "If a patient has already made payment for a regular radiographic guide, is an additional fee required for obtaining a digital radiographic guide?",
            "Can you provide clarification on whether patients need to make an extra payment for a digital radiographic guide if they have already paid for a regular one?",
            "If a patient has already fulfilled the financial obligations for a regular radiographic guide, do they need to pay an extra amount for acquiring a digital radiographic guide?" 
        ],

        "responses":[
            "No. The patient only pays one at a time."
        ]
        
      },
      {
        "tag":"IOD_Treatment_Plan_Panaromic",
        "patterns":
        [
            "Do I need to update the PANORAMIC XRAY for the patient before IOD consult?",
            "Is it necessary to obtain an updated panoramic X-ray for the patient prior to the IOD consultation?",
            "Can you provide guidance on whether a recent panoramic X-ray is required before scheduling an IOD consult for the patient?",
            "Are there any specific imaging requirements or recommendations, such as updating the panoramic X-ray, before proceeding with the IOD consultation?"
        ],

        "responses":[
            "You do not need to get a new PAN since the process of completing the IOD consult includes obtaining a CBCT with the radiographic guide. However, updating the images might still be recommended as needed and indicated in case the CBCT was not taken during the consult process."
        ]
        
      },
      {
        "tag":"IOD_Treatment_Plan_Denture",
        "patterns":
        [
            "Can the IOD implants be placed before fabricating the denture?",
            "Is it possible to perform the placement of IOD implants before fabricating the denture?",
            "Are there any specific considerations or factors to evaluate before deciding whether to place IOD implants prior to denture fabrication?",
            "Is it within the treatment protocol to proceed with the implant placement for IOD before initiating the denture fabrication process?"    
        ],

        "responses":[
            "The UG implant clinic IOD protocol requires completing the IOD consult after denture fabrication. However, if a temporary(interim) full denture was fabricated, you can discuss with the implant faculty the possibility of using it for starting the IOD implant process prior to fabricating the final definitive denture."
        ]
        
      },
      {
        "tag":"About_Radiographic_Guide_CBCT"
        ,
        "patterns":
        [
            "How should I make the radiographic guide?",
            "What is the recommended procedure for fabricating a radiographic guide?",
            "Can you provide guidance on the appropriate steps to follow when making a radiographic guide?",
            "What are the key considerations and techniques involved in the fabrication of a radiographic guide?",
            "Are there any specific materials or tools that should be utilized during the process of creating a radiographic guide?"

        ],

        "responses":[
            "Please review the implant course presentation from your blackboard. It shows detailed step-by-step how to make radiographic guide."
        ]
        
      },
      {
        "tag":"About_Radiographic_Guide_CBCT_Barium",
        "patterns":
        [
            "From whom should I get the barium sulfate?",
            "Who is the appropriate source or supplier for obtaining barium sulfate?",
            "Is there a preferred supplier or manufacturer for barium sulfate that is commonly used in dental practices?"
        ],

        "responses":[
            "You can get the barium sulfate from Faby in Room 321A."
        ]
        
      },
      {
        "tag":"About_Radiographic_Guide_CBCT_Patient",
        "patterns":
        [
            "Who should I ask for if patient is ready for CBCT?",
            "Who should I consult to determine if a patient is ready for a CBCT (Cone Beam Computed Tomography) scan?",
            "Can you provide guidance on the appropriate person or department to contact when assessing a patient's eligibility for a CBCT scan?",
            "Are there specific individuals or roles within the healthcare team who have the authority to determine if a patient is ready for a CBCT scan?"   
        ],

        "responses":[
            "You need to make 1 hour appointment in the implant clinic. Fabi will take the CBCT for your patient. Please make sure that you have the radiographic guide with barium sulfate ready for the CBCT."
        ]
        
      },
      {
        "tag":"About_Radiographic_Guide_CBCT_Review_Scans",
        "patterns":
        [
            "How can I review the CBCT?",
            "What are the methods or tools available to review CBCT (Cone Beam Computed Tomography) scans?",
            "Can you provide guidance on how to effectively review and interpret CBCT images?",
            "What are the recommended software programs or platforms for reviewing CBCT scans?",
            "Are there specific steps or protocols to follow when reviewing CBCT images to ensure accurate interpretation?",
            "Can you outline the process or workflow for reviewing CBCT scans, including any necessary adjustments or settings to optimize image visualization and analysis?"   
        ],

        "responses":[
            "You need to review the CBCT with implant faculty. The implant faculty will show you how to open the CBCT."
        ]
        
      },
      {
        "tag":"About_Radiographic_Guide_CBC_Faculty_Approval",
        "patterns":
        [
            "What should I do after faculty reviews CBCT and approves patient?",
            "After the faculty reviews the CBCT scan and approves the patient, what are the next steps in the treatment process?",
            "Can you provide guidance on the course of action to be taken once the faculty has reviewed and approved the CBCT scan for the patient?",
            "What are the specific actions or procedures that should be followed after the CBCT scan has been reviewed and approved by the faculty?",
            "Can you outline the treatment protocol or workflow to be followed after the faculty's review and approval of the CBCT scan, including any necessary communication or coordination with other healthcare professionals?"
        ],

        "responses":[
            "First, you need to write down your CBCT finding in the Axium. For example: Buccal Lingual width, vertical distances and recommended implant. Please send an Axium message to Predoctoral Implant Program    stating that the patient (including patient   s name, chart number and tooth number) is ready for implant placement. Upon receipt, this message will go to Fabi, who will then assign the patient to a PG resident for an implant surgical consultation."
        ]
        
      },
      {
        "tag":"About_Schedule_Assign_Patient",
        "patterns":
        [
            "My patient was already assigned, who do I contact if they have not scheduled the surgical consult?",
            "If my patient has been assigned for treatment but has not scheduled the surgical consult, whom should I contact to address this issue?",
            "Can you provide guidance on whom I should reach out to if a patient who has already been assigned for treatment has not yet scheduled the surgical consult?",
            "What is the recommended course of action if a patient who has been assigned for treatment has not made arrangements for the surgical consult?",
            "In such cases, whom should I notify or contact to help facilitate the scheduling of the surgical consult for a patient who has already been assigned for treatment?",
            "Who do I send the message to once my patient is ready for assignment?"
        ],

        "responses":[
            "Please send an Axium message to  Predoctoral Implant Program and CC: Sharon Arrigo <sarrig1@uic.edu> for OS, Stephanie Clarke <clarkes@uic.edu> for Prostho and Estefania Martinez <emarti63@uic.edu> for Perio."
        ]
        
      },
      {
        "tag":"About_Schedule_Assign_Patient_Message",
        "patterns":
        [
            "Who do I send the message to once my patient is ready for assignment?",
            "After my patient is ready for assignment, to whom should I send the message or notification?",
            "Can you provide guidance on whom I should contact or notify once my patient is prepared for assignment?",
            "Are there specific individuals or departments that should receive the message when my patient is ready for assignment?",
            "What is the appropriate communication channel or contact point for notifying the relevant parties that my patient is ready for assignment?",
            "What information should I include in the message?"   
        ],

        "responses":[
            "Please send an Axium message to Predoctoral Implant Program. Faby will be the one to receive the message and carry out the assignment."
        ]
        
      },
      {
        "tag":"About_Schedule_Assign_Patient_Message_Detail",
        "patterns":
        [
            "What information should I include in the message?",
            "When sending a message, what specific information should be included to ensure clear communication?",
            "Can you provide guidance on the essential details that should be incorporated into the message to convey the necessary information effectively?",
            "Are there any key elements or data points that must be communicated in the message to ensure a smooth and efficient assignment process?"
        ],

        "responses":[
            "Patient name, chart number and tooth number for implant placement. If your faculty wants to send the patient to specific department, please specify the department name."
        ]
        
      },
      {
        "tag":"About_Schedule_Reply",
        "patterns":
        [
            "What should I expect after I sent the message for surgical assignment?",
            "Once you have sent the message for surgical assignment, what should you anticipate in terms of next steps or responses?",
            "Can you provide guidance on what to expect after sending the message for surgical assignment?",
            "Are there any specific actions or information you should anticipate after sending the message for surgical assignment?"   
        ],

        "responses":[
            "You can check the Axium and will know the PG resident who is going to place the implant after the surgical consult. The PG resident may request the surgical/radiographic guide from you. You can also ask for assisting or observing the implant surgery."
        ]
        
      },
      {
        "tag":"About_STI_Protocol_Oppose",
        "patterns":
        [
            "Can I treat implants opposing to each other?",
            "Is it permissible to provide treatment involving implants that oppose each other?",
            "Can you provide guidance on whether it is acceptable to treat implants that are in an opposing position?",
            "Are there any specific considerations or limitations when considering treatment for implants that are opposing each other?",
            "Is it within the scope of practice to perform procedures involving implants that are in an opposing relationship?"   
        ],

        "responses":[
            "Yes you can."
        ]
        
      },
      {
        "tag":"STI_Appointment_Treatments",
        "patterns":
        [
            "How many appointments do I need to schedule for STI treatments?",
            "What is the recommended number of appointments that should be scheduled for STI treatments?",
            "Can you provide guidance on the appropriate amount of appointments to allocate for STI treatments?",
            "How many separate appointments should be scheduled to ensure a comprehensive and successful STI treatment?"
        ],

        "responses":[
            "You will need 6 appointments to be scheduled in Chicago implant clinic as follows: 1.Initial UG STI consultation. 2.CBCT and finalization of the treatment plan. 3.Final implant impression, once implant is ready for it. 4.Custom abutment try-in. 5.Final crown cementation and delivery. 6.1 week follow-up."
        ]
        
      },
      {
        "tag":"STI_Appointment_Payment",
        "patterns":
        [
            "When do my patients need to pay for the STI abutment and crown?",
            "At what point in the treatment process should patients be expected to make payment for the STI abutment and crown?",
            "Can you provide guidance on when patients should be requested to pay for the STI abutment and crown during their treatment?",
            "What is the designated timeframe or sequence for collecting payment from patients for the STI abutment and crown?"   
        ],

        "responses":[
            "Your patient needs to pay for the STI abutment and crown when you completed the impression. You need to complete DD6057A and B and DD6058A and B."
        ]
        
      },
      {
        "tag":"About_STI_Protocol_Payment_Plan",
        "patterns":
        [
            "Is there any payment plan?",
            "Are there any payment options or installment plans available for patients?",
            "Can you provide information on whether a payment plan is offered for the treatment fees?",
            "What are the available options for patients who require a payment plan to manage the cost of treatment?",
            "Is there a structured payment plan or financial assistance program that can be utilized by patients?"
        ],

        "responses":[
            "Unfortunately, there is not any treatment plan. However, the implant treatment is going to take approximately 6-12 months."
        ]
        
      },   {
        "tag":"About_STI_Protocol_Discount",
        "patterns":
        [
            "Will there be any discount for student or student family's members needing a STI crown?",
            "Is there a discounted rate or special pricing available for students or immediate family members who require a STI crown?",
            "Can you provide information on whether there is a discounted fee for STI crowns specifically for students or their family members?",
            "Do students or their family members qualify for any financial benefits or reduced fees when receiving a STI crown?"  
        ],

        "responses":[
            "There is not treatment discount for student or student family's members needing a STI crown"
        ]
        
      },
      {
        "tag":"STI_Appointment_Duration_Abutment",
        "patterns":
        [
            "How long does it take for the abutment to be ready, after I submit the lab prescription?",
            "Can you provide an estimate of the duration it takes for the abutment to be prepared once the lab prescription has been submitted?",
            "In terms of production and processing, how long should I expect to wait for the abutment to be ready following the submission of the lab prescription?",
            "Can you outline the general timeline or expected waiting period for the fabrication of the abutment after the lab prescription has been sent?"
        ],

        "responses":[
            "It usually takes between 2 to 3 weeks to receive the abutment. Therefore, it is recommended to schedule any subsequent appointments no sooner than 3 weeks following the submission of the lab script. Please make sure you ask digital lab if your abutment/crown is ready before you see your patient."
        ]
        
      }
     
    ]


collection.insert_many(intents_data)