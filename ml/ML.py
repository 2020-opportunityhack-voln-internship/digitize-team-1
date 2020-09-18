import os
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import time
import webbrowser

# Both config and weights need to be from a 3-channel generated model
directory=os.getcwd()
#print(directory[-2:])
if directory[-2:]=='ml':
    file_config = "yolov3-voc.cfg"
    file_weights = "yolov3-voc_best.weights"
elif directory[-15:]=='digitize-team-1':
    file_config = directory+"\\ml\\yolov3-voc.cfg"
    file_weights = directory+"\\ml\\yolov3-voc_best.weights"

# Load the weights and configutation to form the pretrained YOLOv3 model
net = cv.dnn.readNetFromDarknet(file_config, file_weights)

layer_names = net.getLayerNames()
layer_names = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

# Get the labels
labels = [
        "textbox",
        "textline",
        "checkbox"
         ]
colors = [
    #textbox - burnt orange
    [204,85,0],
    #textline - neon pink
    [254,1,154],
    #checkbox - royal blue
    [0,35,102]
]
def draw_labels_and_boxes(img, boxes, confidences, classids, idxs, colors, labels):
    # If there are any detections
    if len(idxs) > 0:
        for i in idxs.flatten():
            # Get the bounding box coordinates
            x, y = boxes[i][0], boxes[i][1]
            w, h = boxes[i][2], boxes[i][3]

            # Get the unique color for this class
            color = [int(c) for c in colors[classids[i]]]

            # Draw the bounding box rectangle and label on the image
            cv.rectangle(img, (x, y), (x+w, y+h), color, 2)
            text = "{}:{:.1f}".format(labels[classids[i]], 100*confidences[i])
            #text = "{:.1f}".format(100*confidences[i])
            cv.putText(img, text, (x, y-3), cv.FONT_HERSHEY_COMPLEX, 0.7, [255, 255, 255], 4)
            cv.putText(img, text, (x, y-3), cv.FONT_HERSHEY_COMPLEX, 0.7, color, 2)
    return img


def generate_boxes_confidences_classids(outs, height, width, tconf):
    boxes = []
    confidences = []
    classids = []

    for out in outs:
        for detection in out:
            # Get the scores, classid, and the confidence of the prediction
            scores = detection[5:]
            classid = np.argmax(scores)
            confidence = scores[classid]

            # Consider only the predictions that are above a certain confidence level
            if confidence > tconf:
                box = detection[0:4] * np.array([width, height, width, height])
                centerX, centerY, bwidth, bheight = box.astype('int')

                # Using the center x, y coordinates to derive the top
                # and the left corner of the bounding box
                x = int(centerX - (bwidth / 2))
                y = int(centerY - (bheight / 2))

                print("x: %s, width: %s " % (x, int(bwidth)) )
                print("y: %s, width: %s "% (y, int(bheight)) )
                # Append to list
                boxes.append([x, y, int(bwidth), int(bheight)])
                confidences.append(float(confidence))
                classids.append(classid)

    return boxes, confidences, classids


def infer_image(net, layer_names, height, width, img, colors, labels,
            boxes=None, confidences=None, classids=None, idxs=None, infer=True):
    
    confidence = 0.40 # Change this to a lower value to get more detections where the model is less confident
    threshold = 0.1

    if infer:
        # Contructing a blob from the input image
        blob = cv.dnn.blobFromImage(img, 1 / 255.0, (416, 416),
                        swapRB=True, crop=False)

        # Perform a forward pass of the YOLO object detector
        net.setInput(blob)

        # Getting the outputs from the output layers
        start = time.time()
        outs = net.forward(layer_names)
        end = time.time()


        print (" YOLOv3 took {:6f} seconds".format(end - start))


        # Generate the boxes, confidences, and classIDs
        boxes, confidences, classids = generate_boxes_confidences_classids(outs, height, width, confidence)

        # Apply Non-Maxima Suppression to suppress overlapping bounding boxes
        idxs = cv.dnn.NMSBoxes(boxes, confidences, confidence, threshold)

    if boxes is None or confidences is None or idxs is None or classids is None:
        raise '[ERROR] Required variables are set to None before drawing boxes on images.'

    # Draw labels and boxes on the image
    img = draw_labels_and_boxes(img, boxes, confidences, classids, idxs, colors, labels)

    return img, boxes, confidences, classids, idxs


def htmlWrapper(boxes, confidences, classids, name='TestFile'):
    #This function will create an HTML file to match the ML output
    #The 'name' parameter will have the file name- still not sure how this will be determined
    filename= name+'.html'
    f= open(filename, 'w')
    type=''
    #Start the html string- currently, sets submission to a default page which currently does nothing
    html= """<html>
<form action="./submission_page.php" method="post">
"""
    #Iterate through each classid to create the appropriate input
    for i,x in enumerate(classids):
        #Confidence threshold will be set later- for now, it is 0
        if confidences[i]>=0:
            if (x==1) or (x==0):
                type='text'
            elif x==2:
                type='checkbox'
            html=html+("""    <input type=%s>
    <br>
""" % type)
    #End the html string and write it to the file
    html=html+"""    <input type=submit>
</form>
</html>"""
    f.write(html)
    f.close()
    webbrowser.open(filename)
    return html  
#To-Do:
    #Use coordinates to map each HTML element to its correct location
    #Add confidence check before adding an element
    #Implement a way to determine the filename, and have the HTML submitted to a place where it can be used
    #Add in a step where user input can add in labels



def detect(image_filename):
    name=image_filename[:-4] #Currently, this should append the filename to remove the extension, but only works for 3-letter extensions
    img = cv.imread(image_filename,cv.IMREAD_COLOR)

    try:
        height, width = img.shape[:2]
    except:
        return
    
    
    print(height,"x",width)
    if height <= 400:
        print("Not even trying for small image")
        return
    
    # Original Image
    #plt.rcParams["figure.figsize"] = (30, 20) # (w, h)
    #plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    #plt.imshow(img)
    
    # Do the detection
    frame, boxes, confidences, classids, idxs = infer_image(net, layer_names, height, width, img, colors, labels)
    
    [print("Confidence: %.2f" % x) for x in confidences]
    print("Class IDs: %s" % classids)
    
    # Show detected image
    plt.rcParams["figure.figsize"] = (30, 20) # (w, h)
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.imshow(frame)
    #Create HTML file
    #Currently, this should save under the same name as the image
    htmlWrapper(boxes, confidences, classids, name)
    plt.show()