#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

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
    }
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
    dementia_type = [dementia_type for dementia_type in dementia_types if dementia_type['id'] == dementia_type_id]
    if len(dementia_type) == 0:
        abort(404)
    return jsonify({'dementia_type': dementia_type[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


if __name__ == '__main__':
    app.run(debug=True)