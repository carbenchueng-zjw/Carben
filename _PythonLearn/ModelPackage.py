import torch,onnxruntime as ort,numpy
from torchvision import models
from torch.utils.mobile_optimizer import optimize_for_mobile


#torchscript:部署到服务端给其他语言调用

# model = models.resnet18(weights = models.ResNet18_Weights.IMAGENET1K_V1)
#
# x = torch.randn([1,3,120,120])
# traced_model = torch.jit.trace(model,x)
#
# out_put = traced_model(torch.ones(1,3,100,100))
# print(out_put.shape)

# traced_model.save("trace_resnet18_model.pt")


#ios/android
# model = models.mobilenet_v2(weights = models.MobileNet_V2_Weights.IMAGENET1K_V1)
# model.eval()
#
# x = torch.randn([1,3,100,100])
# model = torch.jit.trace(model,x)
# model_opt = optimize_for_mobile(model)
# model_opt._save_for_lite_interpreter("mobile_net_v2.pt")


#onnx：
# model = models.mobilenet_v2(pretrained = True)
# model.eval()
#
# input_name = ["input"]
# output_name = ["output"]
# x = torch.randn([1,3,100,100])
# torch.onnx.export(model,x,"mov2_onnx.onnx",input_names=input_name,output_names=output_name,verbose=True)

#使用onnx
# session = ort.InferenceSession("mov2_onnx.onnx")
# x = numpy.random.randn(1,3,100,100).astype(numpy.float32)
# output = session.run(None,input_feed={"input":x})
# print(output[0].shape)

#onnx精度查看
#得到pytorch输出的精度
x = torch.randn(1,3,100,100)
model = models.mobilenet_v2(pretrained = True)
x_out = model(x)
x1_out = x_out.detach().cpu().numpy()
# x_out = x_out.numpy()

#得到onnx输出的精度
session = ort.InferenceSession("mov2_onnx.onnx")
onnx_out = x.detach().cpu().numpy()
x2_out = session.run(None,input_feed={"input":onnx_out})

numpy.testing.assert_almost_equal(x1_out,x2_out[0],decimal=3)#decimal：精确到小数点后三位






