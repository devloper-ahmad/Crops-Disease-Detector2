# views.py
from django.shortcuts import render
from django.core.files.storage import default_storage
import tensorflow as tf
import numpy as np
import os
import cv2
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect


def predict_image(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        if image:
            # Save the image temporarily in the media directory

            temp_image_path = default_storage.save(
                'temp\\' + image.name, image)
            # temp_image_path = os.path.join(
            #     settings.MEDIA_ROOT, temp_image_path)
            print('media/'+temp_image_path)
            # Load the TensorFlow model
            model_path = os.path.join(os.path.dirname(__file__), 'my_model.h5')

            # Load the TensorFlow model
            model = tf.keras.models.load_model(model_path)
            # Preprocess the image
            # Preprocess the image
            print(temp_image_path)
            img = cv2.imread('media/'+temp_image_path)
            img = cv2.resize(img, (256, 256))
            test_input = img.reshape((1, 256, 256, 3))  # Normalize the image

            # Make a prediction
            prediction = model.predict(test_input)

            a = int(np.argmax(prediction))
            if a == 2:
               return HttpResponse("<h1>Result:Early Blight</h1> <br><h1>Recommended Medicines</h1> <br><h3 >Gramaxone, Revus, Miravus duo </h3>")
                
            elif a == 0:
               
                return HttpResponse("<h1>Result:Late Blight</h1> <br><h1>Recommended Medicines</h1> <br><h3 >Amistar Top, Isabion ,Miravus duo </h3>")
            elif a == 1:
                a = "Result: Healthy Potato"
            else:
                a = "Result: no Result"
    

            # Remove the temporary image file
            default_storage.delete(temp_image_path)

            # Return the prediction to the frontend
            context = {'prediction': a}
            return render(request, 'prediction.html',context )

    # If it's a GET request or image upload failed, render the upload form
    return render(request, 'upload.html')
