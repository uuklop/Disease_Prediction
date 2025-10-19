from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PatientForm
from .models import PatientDetails
import numpy as np
import joblib as joblib
import pickle
import sklearn

def drugHome(request):
    gender = request.POST.get('gender','')
    agereceived = request.POST.get('age','')
    disease = request.POST.get('disease','')

    # Prepare a list of age options from 16 to 80
    age_options = [str(age) for age in range(16, 81)]

     # Check if any of the required fields is empty
    if not gender or not agereceived or not disease:
        context = {
                'status': "Please fill in all required fields",
                'age_options': age_options,
            }
        return render(request, 'drug_rec/home.html', context)

    try:
        age = int(agereceived)
    except ValueError:
        context = {
                
                'status': "Invalid age value",
            }
        return render(request, 'drug_rec/home.html', context)


    
   
    sick = str(disease)

    if gender == 'Male':
       sex = 1
    else:
      sex = 0

    disease_list = ['Acne','Allergy','Diabetes','Fungal infection','Urinary tract infection','Malaria','Migraine','Hepatitis B','AIDS']
  
    disease_dict = {'Acne':0,'Allergy':1,'Diabetes':2,'Fungal infection':3,'Urinary tract infection':4,'Malaria':5,'Migraine':6,'Hepatitis B':7, 'AIDS':8}

    if sick in disease_list:
        print('AI Got Drug For This Disease')
        print("Scikit-Learn Version:", sklearn.__version__)
        print(disease_dict.get(sick))
        new_sick = disease_dict.get(sick)

          
        test = [new_sick,sex,age]
        print(test)
        test = np.array(test)
        print(test.shape)
        test = np.array(test).reshape(1,-1)
        print(test.shape)

        clf = joblib.load('medical_model.pkl')
        prediction = clf.predict(test)
        prediction = prediction[0]
        print('Predicted Disease Is',prediction)


        context = {
            'gender': gender,
            'age': age,
            'disease': disease,
            'prediction': prediction,
            'age_options': age_options,
        }

        return render(request, 'drug_rec/home.html', context)
    
    else:
        context =  {
            'status':"AI cannot Recommend Drug",
            'age_options': age_options,
        }
        return render(request, 'drug_rec/home.html', context)
    
    # if request.method == 'POST':
    #     form = PatientForm(request.POST)

    #     if form.is_valid():
    #         form.save()
    #         return redirect('details')
    # else:
    #     form = PatientForm()

    # context = {
    #     'form': form,
    # }

    # return render(request, 'drug_rec/home.html', context)

def patientDetail(request):
    pass
#     patients = PatientDetails.objects.all()

#     context = {
#         'patients': patients,
#     }

#     return render(request, 'drug_rec/patient_details.html', context)