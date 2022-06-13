import numpy as np

def myconv(input, kernel, padding=1, stride=1):
    # input [batch, h, w,c]
    # kernel [k_size, k_size, c_in, c_out]
    b, h, w, c = input.shape
    k_size, _, _, c_out = kernel.shape

    if padding > 0:
        input_pad = np.zeros((b, h + 2 * padding, w + 2 * padding, c))
        input_pad[:, padding:-padding, padding:-padding, :] = input
    else:
        input_pad = input

    out_h = int((h - k_size + 2 * padding) / stride + 1)
    out_w = int((w - k_size + 2 * padding) / stride + 1)
    out = np.zeros((b, out_h, out_w, c_out))

    for i in range(out_h):
        for j in range(out_w):
            roi = input_pad[:, i * stride:i * stride + k_size, j * stride:j * stride + k_size, :]     # shape (b,k_size,k_size,c)
            # roi [b,h,w,c]->[b,h,w,c,c_out]
            conv = np.tile(np.expand_dims(roi, -1), (1, 1, 1, 1, c_out)) * kernel   # expand之后 shape (b,k_size,k_size,c,1)   tile之后shape (b,k_size,k_size,c,c_out)
            # [b,h,w,c,c_out]->[b,h,w,c_out]
            out[:, i, j, :] = np.squeeze(np.sum(conv, axis=(1, 2, 3), keepdims=True), axis=(1, 2, 3))  # conv shape (b,k_size,k_size,c,c_out)  sum之后shape (b,1,1,1,c_out)  squeeze之后shape (b, 1, 1, c_out)
            # out[:, i, j, :]切片出来的是一个二位数组out[:, :], 当前维度为段才会保留维度，为数维度变为1默认缩调，类似 out[n, i, j, m]切片出来是个数

    return out

input_data = [[[1,0,1,2,1],[0,2,1,0,1],[1,1,0,2,0],[2,2,1,1,0],[2,0,1,2,0]],
              [[2,0,2,1,1],[0,1,0,0,2],[1,0,0,2,1],[1,1,2,1,0],[1,0,1,1,1]],]    # shape (2,5,5)
weight = [[[1,0,1],[-1,1,0],[0,-1,0]],[[-1,0,1],[0,0,1],[1,1,1]]]   # shape (2,3,3)

input = np.array(input_data)
input = input.transpose((1, 2, 0))     # shape (5,5,2)
input = np.expand_dims(input, 0)     # shape (1,5,5,2)
input = np.tile(input,(1, 1, 1, 1))     # shape (8,5,5,2)

kernel = np.array(weight)               # shape (2,3,3)
kernel = kernel.transpose((1,2,0))       # shape (3,3,2)
kernel = np.expand_dims(kernel,-1)     # shape (3,3,2,1)
kernel = np.concatenate((kernel,kernel),3)   # shape (3,3,2,2)

out = myconv(input,kernel)
