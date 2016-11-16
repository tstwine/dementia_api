#!flask/bin/python
from flask import Flask, jsonify, render_template, flash, request, url_for, redirect
from flask import abort
from flask import make_response
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
auth = HTTPBasicAuth()

# import alzheimers
alzheimers = []
name = []

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    text = db.Column(db.Text)
    timeposted = db.Column(db.DateTime)

    def __init__(self, name, text):
        self.name = name
        self.text = text
        self.timeposted = datetime.now()

    def __repr__(self):
        return '<Comment %r, %r, %r>' % (self.name, self.text, self.timeposted)

    

alzheimers_data = {
        'question':'What do you want to know about the different types of dementia?',
       'fields': [ """Alzheimer's Disease""",
                   'Vascular Dementia',
                   'Dementia_with_Lewy_bodies',
                   'Mixed_Dementia',
                   'Parkinsons',
                   'Creutzfeldt_Jakob_Disease',
                   'Normal_Pressure_Hydrocephalus']
    }

dementia_types = [
    {
        'id': 1,
        "name": "Alzheimer's Disease",
        "definition": """Alzheimer's disease is an irreversible, progressive brain disorder that slowly destroys memory and thinking skills and, 
                     eventually, the ability to carry out the simplest tasks. In most people with Alzheimer's, symptoms first appear in their mid-60s. 
                     Alzheimer's disease is the most common cause of dementia among older adults.""",
        "diagnosis": """Ask the person and a family member or friend questions about overall health, past medical problems, ability to carry out 
                     daily activities, and changes in behavior and personality, conduct tests of memory, problem solving, attention, counting, and language,
                     Conduct tests of memory, problem solving, attention, counting, and language,
                     Carry out standard medical tests, such as blood and urine tests, to identify other possible causes of the problem,
                     Perform brain scans, such as computed tomography (CT), magnetic resonance imaging (MRI), or positron emission tomography (PET), 
                     to rule out other possible causes for symptoms.""",
        "symptons": """The symptoms of Alzheimer's vary from person to person. For many, decline in non-memory aspects of cognition, such as 
                    word-finding, vision/spatial issues, and impaired reasoning or judgment, may signal the very early stages of Alzheimer's disease. 
                    Researchers are studying biomarkers (biological signs of disease found in brain images, cerebrospinal fluid, and blood) to see if 
                    they can detect early changes in the brains of people with MCI and in cognitively normal people who may be at greater risk for 
                    Alzheimer's. Studies indicate that such early detection may be possible, but more research is needed before these techniques can be 
                    relied upon to diagnose Alzheimer's disease in everyday medical practice.""",
        "types": """Mild Alzheimer's Disease people experience greater memory lss and other cognitive difficulties. Problems can 
                    include wandering and getting lost, trouble handling money and paying bills, repeating questions, taking longer to complete normal 
                    daily tasks, and personality and behavior changes. People are often diagnosed in this stage.,
                    Moderate Alzheimer's Disease damage occurs in areas of the brain that control language, reasoning, sensory processing, 
                    and conscious thought. Memory loss and confusion grow worse, and people begin to have problems recognizing family and friends. 
                    They may be unable to learn new things, carry out multistep tasks such as getting dressed, or cope with new situations.
                    People at this stage may have hallucinations, delusions, and paranoia and may behave impulsively.
                    Severe Alzheimer's Disease plaques and tangles spread throughout the brain, and brain tissue shrinks significantly. People with 
                    severe Alzheimer's cannot communicate and are completely dependent on others for their care. Near the end, the person may be in 
                    bed most or all of the time as the body shuts down.""",
        "treatments":"""No treatment is available to slow or stop Alzheimer's disease. The U.S. Food and Drug Administration has pproved five drugs that 
                    temporarily improve symptoms. The effectiveness of these drugs varies available today alters the underlying course of this terminal disease. 
                    Researchers around world are studying dozens of treatment strategies that may have the potential to change."""

    },
    {
        'id': 2,
        "name":"Vascular Dementia",
        "definition":"""Vascular dementia is considered the second most common form of dementia after Alzheimer's disease, results from interrupted blood flow to the brain, often 
                     after a stroke or series of strokes. The symptoms can be similar to those of Alzheimer's, and both conditions can occur at the same time. 
                     Inadequate blood flow can damage and eventually kill cells anywhere in the body results from conditions, such 
                     results from conditions, such as high blood pressure and high cholesterol, that can damage blood vessels in the brain.
                     as high blood pressure and high cholesterol, that can damage blood vessels in the brain.""",
        "diagnosis":"""Individuals at highest risk include those who have had a stroke or a transient ischemic attack (TIA, also known as a "ministroke"). 
                    Additional high-risk groups include those with high blood pressure, high cholesterol, or other risk factors for heart or blood vessel disease.
                    A thorough medical history, including family history of dementia. Evaluation of independent function and daily activities, input from a family
                    member or trusted friend. In-office neurological examination assessing function of nerves and reflexes, movement, coordination, balance and senses.
                    Laboratory tests including blood tests and brain imaging.""",
        "symptoms":"""Symptoms can vary widely, depending on the severity of the blood vessel damage and the part of the brain affected. Memory loss may or may 
                    not be a significant symptom depending on the specific brain areas where blood flow is reduced. Major symptons are confusion, disorientation, 
                    trouble speaking or understanding speech, and vision loss.""",
        "treatments":"""Controlling risk factors that may increase the likelihood of further damage to the brain's blood vessels is an important treatment strategy. 
                    There's substantial evidence that treatment of risk factors may improve outcomes and help postpone or prevent further decline.""",

        "causes":"""The cause and risk factors are to keep your blood pressure, cholesterol and blood sugar within recommended limits."""
    },

    {

    'id': 3,
    "name":"Dementia_with_Lewy_bodies",
    "definition":"""definition":Dementia with Lewy bodies (DLB) is a type of progressive dementia that leads to a decline in thinking, reasoning and independent function 
                 because of abnormal microscopic deposits that damage brain cells over time. Most experts estimate that dementia with Lewy bodies is the 
                 third most common cause of dementia after Alzheimer's disease and vascular dementia.""",
    "diagnosis":"""Dementia symptoms consistent with DLB develop first, when both dementia symptoms and movement symptoms are present at the time of diagnosis,
                     when dementia symptoms appear within one year after movement symptoms.""",
    "symptoms":"""Changes in thinking and reasoning, Confusion and alertness that varies significantly from one time of day to another or from 
                  one day to the next, Parkinson's symptoms, such as a hunched posture, balance problems and rigid muscles, visual hallucinations, delusions, 
                  trouble interpreting visual information, acting out dreams, sometimes violently, a problem known as rapid eye movement (REM) sleep disorder, 
                  malfunctions of the "automatic" (autonomic) nervous system, and memory loss that may be significant but less prominent than in Alzheimer's. """,
    "treatments":"""There are no treatments that can slow or stop the brain cell damage caused by dementia with Lewy bodies""",
    "medications":"""Medications used to treat DLB are Cholinesterase inhibitors drugs are the current mainstay for treating thinking changes in Alzheimer's. 
                      They also may help certain DLB symptoms. Antipsychotic drugs are used for behavioral symptons that can occur in Alzheimer's. Antidepressants
                      may be used to treat depression, which is common wtih DLB, Parkinson's disease dementia and Alzheimer's. Clonazepam may be prescribed to treat
                      REM sleep disorder. """,

    },

    {

    'id': 4, 
    "name":"Mixed_Dementia",
    "definition":"""Mixed dementia is a condition in which abnormalities characteristic of more than one type of dementia occur simultaneously. 
                 Mixed dementia is also knowns as multifactorial. In the most common form of mixed dementia, the abnormal protein deposits associated 
                 with Alzheimer's disease coexist with blood vessel problems linked to vascular dementia. Alzheimer's brain changes also often coexist 
                 with Lewy bodies. In some cases, a person may have brain changes linked to all three conditions-Alzheimer's disease, vascular dementia .""",
    "diagnosis":"""A diagnosis of mixed dementia comes after a brain autopsy. Most individuals whose autopsies show they had mixed dementia were 
                diagnosed with one specific type of dementia during life, most commonly with Alzheimer's disease. The most common coexisting abnormality 
                was previously undetected blood clots or other evidence of vascular disease. Lewy bodies were the second most common coexisting abnormality.""",
    "symptons":"""Mixed dementia symptoms may vary, depending on the types of brain changes involved and the brain regions affected. In many cases, 
                symptoms may be similar to or even indistinguishable from those of Alzheimer's or another type of dementia. In other cases, a person's 
                symptoms may suggest that more than one type of dementia is present.""",
    "causes":"""Mixed dementia is infrequently diagnosed during life, many researchers believe it deserves more attention because the combination of two 
                or more types of dementia-related brain changes may have a greater impact on the brain than one type alone. Evidence suggests that the 
                presence of more than one type of dementia-related change may increase the chances a person will develop symptoms.""",
    "treatments":"""Because most people with mixed dementia are diagnosed with a single type of dementia, physicians often base their prescribing decisions on 
                    the type of dementia that's been diagnosed.""",
    },


    {
    'id': 5,
    "name":"Parkinsons",
    "definition":"""Parkinson's disease is an impairment in thinking and reasoning. The brain changes caused by Parkinson's disease begin in 
                 a region that plays a key role in movement. As Parkinson's brain changes gradually spread, they often begin to affect mental functions, including 
                 memory and the ability to pay attention, make sound judgments and plan the steps needed to complete a task. The key brain changes linked to Parkinson's
                 disease and Parkinson's disease dementia are abnormal microscopic deposits composed chiefly of alpha-synuclein, a protein that's found widely in the 
                 brain but whose normal function isn't yet known. The deposits are called "Lewy bodies""",
    "diagnosis":"""A person diagnosed with Parkinson's based on movement symptoms and dementia symptoms don't appear until a year or more later. The 
                diagnosis is dementia with Lewy bodies when dementia appear within one year after movement symptoms. When movement symptoms develop within
                a year of a dementia with Lewy bodies diagnosis.""",
    "symptoms":"""Changes in memory, concentration and judgment, trouble interpreting visual information, Muffled speech, Visual hallucinations,
                Delusions, especially paranoid ideas, depression, Irritability and anxiety, and Sleep disturbances, including excessive daytime drowsiness 
                and rapid eye movement (REM) sleep disorder.""",
    "causes":"""Certain factors at the time of Parkinson's diagnosis may increase future dementia risk, including older age, greater severity of motor symptoms, 
                and having mild cognitive impairment (MCI).""",

    "treatments":"""Cholinesterase inhibitors, antipsychotic drugs, L-dopa, antidepressants, clonazepam."""

    },

        {
    'id': 7,
    "name":"Creutzfeldt_Jakob_Disease",
    "definition":"""Creutzfeldt-Jakob disease (CJD) is the most common human form of a group of rare, fatal brain disorders known as prion diseases.
                Creutzfeldt-Jakob disease causes a type of dementia that gets worse unusually fast. More common causes of dementia, such as Alzheimer's, 
                dementia with Lewy bodies and frontotemporal dementia, typically progress more slowly. Prion diseases, such as Creutzfeldt-Jakob disease, 
                occur when prion protein, which is found throughout the body but whose normal function isn't yet known, begins folding into an abnormal 
                three-dimensional shape. This shape change gradually triggers prion protein in the brain to fold into the same abnormal shape. """,
    "diagnosis":"""Rapid symptom progression is one of the most important clues that a person may have Creutzfeldt-Jakob disease. These test may help 
                determine whether an individual has CJD are Electroencephalogram (EEG) measures the brain's patterns of electrical activity similar to 
                the way an electrocardiogram (ECG) measures the heart's electrical activity. Brain magnetic resonance imaging (MRI) can detect certain 
                brain changes consistent with CJD. Lumbar puncture (spinal tap) tests spinal fluid for the presence of certain proteins. """,
    "symptoms":"""Depression, agitation, apathy and mood swings, rapidly worsening confusion, disorientation, and problems with memory, thinking, 
               planning and judgment, diffiuclty walking and muscle stiffness, twitches and involuntary jerky movement. """,
    "causes":"""Creutzfeldt-Jakob disease has no known cause. Most scientists believe the disease begins when prion protein somewhere in the brain 
             spontaneously misfolds, triggering a "domino effect" that misfolds prion protein throughout the brain. Genetic variation in the prion 
             protein gene may affect risk of this spontaneous misfolding. """,
    "treatments":"""There is no treatment that can slow or stop the underlying brain cell destruction caused by Creutzfeldt-Jakob disease and 
                 other prion diseases. Various drugs have been tested but have not shown any benefit. Clinical studies of potential CJD treatments 
                 are complicated by the rarity of the disease and its rapid progression. """,

    },


    {
    'id': 8,
    "name":"Normal_Pressure_Hydrocephalus",
    "definition":"""Normal Pressure Hydrocephalus is a brain disorder in which excess cerebrospinal fluid Normal pressure hydrocephalus is a 
                brain disorder in which excess cerebrospinal fluid. Normal pressure hydrocephalus occurs when excess cerebrospinal fluid accumulates in 
                the brain's ventricles, which are hollow fluid-filled chambers. NPH is called "normal pressure" because despite the excess fluid, cerebrospinal
                fluid pressure as measured during a spinal tap is often normal. As brain ventricles enlarge with the excess cerebrospinal fluid, they can 
                disrupt and damage nearby brain tissue.""",
    "diagnosis":"""There is no single test to determine if someone has normal pressure hydrocephalus. And even though the three hallmark symptoms 
                listed above are considered the "classic" signs of this disorder, not everyone with NPH has all of these symptoms.
                Difficulty walking that is sometimes compared to the way a person walks on a boat, with the body bent forward legs held wide apart and feet,
                apathy, impaired planning and decision-making, reduced concentration and changes in personality and behavior. Loss of bladder control, which tends to 
                appear somewhat later in the disease than difficulty walking and cognitive decline.""",
    "causes":"""Normal Pressure Hydrocephalus may be caused by other brain disorders such as hemorrhages, infections, inflammation or fluid-filled
                fluid-filled buildup happens for unknown reasons.""" ,
    "treatments":"""NPH can sometimes be treated with surgical insertion of a shunt, a long, thin tube that drains excess CSF from the brain to the abdomen. 
                Difficulty walking is the symptom most likely to improve after surgery. Thinking changes and bladder control are less likely to get better. 
                Shunting doesn't help everyone with NPH, and there's uncertainty about how best to identify those most likely to benefit. """,
    },

]

@auth.get_password
def get_password(username):
    if username == 'tina':
        return 'dementia'
    return None



@app.route('/dementia_types', methods=['GET'])
@auth.login_required
def get_dementia_types():
    return jsonify({'dementia_types': dementia_types})


@app.route('/dementia_types/<int:dementia_type_id>', methods=['GET'])
@auth.login_required
def get_dementia_type(dementia_type_id):

    for dementia_type in dementia_types:
        if dementia_type['id'] == dementia_type_id:
            return jsonify({'dementia_type': dementia_type})

    abort(404)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

    
     

@app.route('/')
def home():

    comments = Comment.query.all()
    
    return render_template('home.html', alzheimers=alzheimers_data, dementia_types=dementia_types, comments=comments)

@app.route("/information/<subject>")
def information(subject):  
    return  render_template('information.html', information=information)

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/comment', methods=['GET', 'POST'])
def createComment():

    name = request.form.get("name")
    text = request.form.get("text")
    comment = Comment(name, text)
    db.session.add(comment)
    db.session.commit()

    return render_template('comment.html', comment=comment)



if __name__ == '__main__':
    app.run(debug=True)
    



    