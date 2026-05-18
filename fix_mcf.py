with open('mcf', 'rb') as f:
    data = f.read()
data = data.replace(b'\r\n', b'\n')
with open('mcf', 'wb') as f:
    f.write(data)
print('Fixed mcf line endings')
