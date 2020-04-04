from django.shortcuts import render, get_object_or_404, redirect
from .forms import DocumentForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Document
from django.conf import settings
import os
from .main import sam
import numpy as np
import tensorflow as tf
import cv2
import time
import glob
from progressbar import *
widgets = [Bar('>'), ' ', ETA(), ' ', ReverseBar('<')]
pbar = ProgressBar(widgets=widgets, maxval=10000000)
class People_Counter:

    def __init__(self, path):
        self.path = path
        self.detection_graph = tf.Graph()
        with self.detection_graph.as_default():
            od_graph_def = tf.GraphDef()
            with tf.gfile.GFile(self.path, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')

        self.default_graph = self.detection_graph.as_default()
        self.sess = tf.Session(graph=self.detection_graph)

        self.image_tensor = self.detection_graph.get_tensor_by_name('image_tensor:0') # Defining tensors for the graph
        self.detection_boxes = self.detection_graph.get_tensor_by_name('detection_boxes:0') # Each box denotes part of image with a person detected
        self.detection_scores = self.detection_graph.get_tensor_by_name('detection_scores:0') # Score represents the confidence for the detected person
        self.detection_classes = self.detection_graph.get_tensor_by_name('detection_classes:0')
        self.num_detections = self.detection_graph.get_tensor_by_name('num_detections:0')

    def detect(self, image):
        image_np_expanded = np.expand_dims(image, axis=0)
        (boxes, scores, classes, num) = self.sess.run(
            [self.detection_boxes, self.detection_scores, self.detection_classes, self.num_detections],
            feed_dict={self.image_tensor: image_np_expanded}) # Using the model for detection

        im_height, im_width,_ = image.shape
        boxes_list = [None for i in range(boxes.shape[1])]
        for i in range(boxes.shape[1]):
            boxes_list[i] = (int(boxes[0,i,0] * im_height),
                        int(boxes[0,i,1]*im_width),
                        int(boxes[0,i,2] * im_height),
                        int(boxes[0,i,3]*im_width))

        return boxes_list, scores[0].tolist(), [int(x) for x in classes[0].tolist()], int(num[0])

    def close(self):
        self.sess.close()
        self.default_graph.close()

def mlmodel(request):
    v = sam()
    print (v)
    for files in os.walk('results/'):
       print(files)

    context['s'] = v
    context = dict()
    i = 0
    for file in files[2]:
        context[i] = 'results/' + file
        print('backend/results/' + file)
    return render(request,'crisis/mlmodel.html',context)

def special(request,pk):
    obj = get_object_or_404(Document,pk=pk)
    return render(request,'crisis/special.html',{'source':obj})

def index(request):
    obj = Document.objects.all()
    return render(request,'crisis/index.html',{'obj':obj})

def register(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.cleaned_data.get("document")
            name = form.cleaned_data.get("name")
            newobj = Document(document=profile,name=name,description="0")
            newobj.save()
            return redirect('index')
    else:
        form = DocumentForm()
    return render(request, 'crisis/registration.html', {
        'form': form
    })
