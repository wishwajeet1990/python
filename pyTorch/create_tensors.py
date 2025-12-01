import torch

a = torch.tensor([1, 2, 3])
b = torch.zeros((3,3))
c = torch.randn((2,2))
print(a)
print(b)
print(c)

print("Other statement")
t = torch.randn((2,3))
print(t)
print(t.shape)

# reshape
t2 = t.reshape(3,2)
print(t2)


x = torch.tensor([10, 20, 30], dtype=torch.float32)
y = torch.tensor([1, 2, 3], dtype=torch.float32)

print("x + y =", x + y)
print("x * y =", x * y)
print("Mean =", x.mean())
print("Max =", x.max())
print("Sum =", x.sum())

device = "cuda" if torch.cuda.is_available() else "cpu"
print(device)
x = torch.randn(10000,10000)
print(x)