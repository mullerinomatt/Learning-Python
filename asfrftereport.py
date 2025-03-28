#'LIHWAP':	[],#
#'Sexual Risk Avoidance Education':	[],#

#added these manually
#G99THV1	Tribal MIECHV - S &B
#G991051	PDG Salaries & Benefits
#G990131	ARP FVPSA Testing S&B
#G99UES5	UC S+B - External (ORR-funded staff)
#G990210	FVPS (Programs for Survivors) Discretionary
#G996143	RESP. FATHERHOOD SALARY & BENE
#G99UGS3	UC - Settlement Staffing
#G9924TA	CHILD SUPPORT T&TA HEADQUARTERS


OLAB = {
'LIHEAP':	['G992230'],
'Transitional and Medical Services':	['G99TMS5','G99TMS4','G99TMS3','G994014'],
'Unaccompanied Children':	['G99UES5','G99UGS3','G990506','G99UCD5','G99GCU5','G99USB4','G99BDU4','G99UCD4','G99GCU4','G99LSB4','G99OMS4','G99SBU3','G99BDU3','G99GCU3','G99OLSB'],
'Victims of Trafficking':	['G99USQ5'],
'Victims of Torture':	['G992198'],
'Child Care and Development Block Grant':	['G99WRGK','G993020','G999018'],
'Head Start':	['G991111','G993140','G991131'],
'Preschool Development Grant':	['G991051','G991052','G992109'],
'Runaway and Homeless Youth Programs':	['G994223','G994222','G998049','G998048'],
'Service Connection for Youth on the Streets':	['G995557','G995556'],
'Family Violence Prevention and Services':	['G991542','G991541','G995346','G990131','G990210'],
'Community Services Block Grant':	['G994016','G993144','G990183'],
'Chafee Education & Training Vouchers':	['G992600','G992604'],
'Disaster Human Services Case Management':	['G99CMSB','G99018'],
'Federal Administration':	['G990166','G996462','G996477','G996413','G996473','G996469','G996468','G996467','G996465','G996461','G996456','G996440','G996435','G996430','G996416','G996415','G996411','G996407','G996406','G996403','G996402','G996401','G105201','G095201','G085201','G075201','G065201','G055201','G045201','G035201','G025201','G015201'],

'Promoting Safe and Stable Families':	['G990595','G990594'],
'Personal Responsibility Education Program':	['G99SR25','G99SV25'],

'Foster Care Prevention & Permanency':	['G994418','G994416','G990193','G994108'],
'Childrens Research & Technical Assistance':	['G9924TA','G9925TB','G9925FB','G990592'],
'Welfare Research':	['G996148','G996190','G990192','G99CS25'],
'Home Visiting': ['G99THV1'],
'Temporary Assistance for Needy Families':	['G996143','G996124','G996147','G990191','G990189','G990197']


    }

#use this to flip the list
OLAB2 = {}
for key, value_list in OLAB.items():
    for value in value_list:
        if value not in OLAB2:
            OLAB2[value] = []
        OLAB2[value].append(key)

#output report with categories
import pandas as pd
df = pd.read_csv('FTEreport.csv')
df['CAN1Map'] = df['CAN1'].map(OLAB2)
df['CAN2Map'] = df['CAN2'].map(OLAB2)
df['CAN3Map'] = df['CAN3'].map(OLAB2)
df['concatenate'] = df['CAN1Map'] + df['CAN2Map'] + df['CAN3Map']
df.to_csv('asfrftereportmapping.csv', index=False)