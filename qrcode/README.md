## Quick Start

这是一个python脚本，依赖于`qrtools`、`zbar`、`qrcode`以及`PIL`库，`zbar`安装相对比较复杂，因此写了一个`Dockerfile`，只要在本地安装`Docker`，环境的事一切交给`Docker`去完成吧!

快速生成一个二维码，二维码数据为`"Hello World!"`:

```bash
./qr encode --data "Hello World" -o helloworld.png
```

输出如下:

![hello world](./helloworld.png)

解析二维码数据:

```bash
./qr decode --file helloworld.png
```

输出信息：

```
Hello World!
```

查看帮助信息:

```bash
usage: ./qr [-v] <subcommand> ...

A python app for creating and decoding QR Codes

positional arguments:
  <subcommand>
    bash-completion
    decode         Decode a qrcode, return the data.
    encode         Generate qrcode for the given data.
    help           Display help about this program or one of its subcommands.

optional arguments:
  -v, --version    show program's version number and exit

See "qrcode help COMMAND" for help on a specific comand.
```

## 编译

```
cd qrcode
docker build -t krystism/qrcode .
```

## 运行

```
docker run -t -i --rm -v `pwd`:/root krystism/qrcode
```

