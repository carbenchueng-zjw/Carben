import onnx,torch,tensorflow as tf
from torchvision import models
from onnx_tf.backend import prepare


# net = models.mobilenet_v2(pretrained = True)
# x = torch.randn(1,3,244,244)
# y = net(x)
#
# #将模型导出为onnx
# torch.onnx.export(net,x,"ym2.onnx",input_names=["x"],output_names=["y"])

#简化onnx模型
#安装 pip install onnx-simplifier
#简化onnx：python -m onnxsim input_onnx_model output_onnx_model


# #把onnx转化为tensorflow,为了得到.pb     pip install onnx_tf, tensorflow_probability
# onnx_model = onnx.load("ym2_sim.onnx")
# tf_rep = prepare(onnx_model)
# tf_rep.export_graph("tf_model")
#由pd得到tflife
converter = tf.lite.TFLiteConverter.from_saved_model("tf_model")
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tf_lite_model = converter.convert()
with open("ym2.tfile","wb") as f:
    f.write(tf_lite_model)

