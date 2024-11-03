from django.shortcuts import render, HttpResponse, redirect
from joblib import load

model = load('./savedModels/model.joblib')


# Create your views here.
def model_home(request):

    if request.method == 'POST':
        sepal_length = float(request.POST['sepal_length'])
        sepal_width = float(request.POST['sepal_width'])
        petal_length = float(request.POST['petal_length'])
        petal_width = float(request.POST['petal_width'])

        # print(f"sepal length: {sepal_length}, sepal_width: {sepal_width}, petal_length: {petal_length}, petal_width: {petal_width}")

        prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])

        print(f'prediction: {prediction}')
    
        if prediction[0] == 0:
            prediction = 'Iris-setosa'
        elif prediction[0] == 1:
            prediction = 'Iris-versicolor'
        else:
            prediction = 'Iris-virginica'

        return render(request, 'predict.html', {'prediction': prediction})

        

    # if method is GET
    return render(request, 'modelHome.html')

  

# def predict(request):
#     sepal_length = float(request.POST['sepal_length'])
#     sepal_width = float(request.POST['sepal_width'])
#     petal_length = float(request.POST['petal_length'])
#     petal_width = float(request.POST['petal_width'])

#     prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])

#     print(f'prediction: {prediction}')
  
#     if prediction[0] == 0:
#         prediction = 'Iris-setosa'
#     elif prediction[0] == 1:
#         prediction = 'Iris-versicolor'
#     else:
#         prediction = 'Iris-virginica'

#     return render(request, 'predict.html', {'prediction': prediction})