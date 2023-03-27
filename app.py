from flask import Flask, request, jsonify
from flask.helpers import send_file
#from PIL import Image
#from transformers import AutoProcessor, AutoModelForCausalLM

app = Flask(__name__, static_url_path='/', static_folder='web')

    
@app.route("/")
def indexPage():
    return send_file("Web/index.html")

@app.route('/upload', methods=['POST'])
def upload_image():
    
    # Get the uploaded image from the request
    image_file = request.files['image']

    #image = Image.open(image_file)
    #processor = AutoProcessor.from_pretrained("microsoft/git-base-coco")
    #model = AutoModelForCausalLM.from_pretrained("microsoft/git-base-coco") 
    #pixel_values = processor(images=image, return_tensors="pt").pixel_values
    #generated_ids = model.generate(pixel_values=pixel_values, max_length=50)
    #generated_caption = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    generated_caption = "Nothing to see here"

    print(generated_caption)
       
    return jsonify({
        "generated_caption": generated_caption,
    })
