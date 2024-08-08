import joblib 
import numpy as np
import pandas as pd
import io
import matplotlib.pyplot as plt
import base64


class Model:
    def Predicit(L):
        DB = {0:"NO DB" , 1:"DB"}
        model = joblib.load("./server/Diabetes.joblib")
        result = model.predict_proba(L)
        print(DB[np.argmax(result)])
        return result

class image_Result:
    def get_image( value):
        color=""
        title = ""
        if value<0.34:
            color="green"
            title = "perfect, no danger"
        elif value<0.68 and value>=0.34:
            color="orange"
            title = "suggested to take precaution"
        elif value<1 and value>=0.68:
            color="red"
            title = "Better consult a doctor"
        fig, ax = plt.subplots()
        ax.barh(['prediction'], [value], color=color)
        ax.set_xlim(0, 1)  # Set x-axis range from 0 to 1
        ax.set_xlabel('severity')
        ax.set_title(title)
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plt.close(fig)

        return buf

# m1 = Model()
# result = m1.Predicit([[1, 89, 66, 23, 94, 28.100000, 0.167000, 21]])
# print(np.argmax(result))
# get_img = image_Result()
# img = get_img.get_image(result[0][1])
# img_str = base64.b64encode(img.getvalue()).decode('utf-8')
# plt.imshow(img_str)
# print(result[0][1])