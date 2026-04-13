---
github_repo: yicheng0|Agent-wiki
github_issue: 1
---
# Docker容器化部署指南

## 概述

Docker是一个开源的容器化平台，允许开发者将应用程序及其依赖项打包到轻量级、可移植的容器中。本文档介绍Docker的核心概念和实际部署流程。

## 核心概念

### 镜像 (Image)
- 只读模板，包含运行应用所需的所有内容
- 通过Dockerfile定义
- 可以从Docker Hub或私有仓库拉取

### 容器 (Container)
- 镜像的运行实例
- 轻量级、隔离的运行环境
- 可以启动、停止、删除

### 仓库 (Registry)
- 存储和分发Docker镜像的服务
- Docker Hub是公共仓库
- 可以搭建私有仓库

## 安装Docker

### Linux系统
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
```

### Windows/Mac
下载Docker Desktop并安装：https://www.docker.com/products/docker-desktop

## 基础命令

### 镜像管理
```bash
# 拉取镜像
docker pull nginx:latest

# 查看本地镜像
docker images

# 删除镜像
docker rmi image_id
```

### 容器操作
```bash
# 运行容器
docker run -d -p 80:80 --name web nginx

# 查看运行中的容器
docker ps

# 停止容器
docker stop web

# 删除容器
docker rm web
```

## Dockerfile示例

创建一个Node.js应用的Dockerfile：

```dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install --production

COPY . .

EXPOSE 3000

CMD ["node", "server.js"]
```

构建镜像：
```bash
docker build -t myapp:1.0 .
```

## Docker Compose

用于定义和运行多容器应用的工具。

### docker-compose.yml示例
```yaml
version: '3.8'

services:
  web:
    image: nginx:latest
    ports:
      - "80:80"
    volumes:
      - ./html:/usr/share/nginx/html

  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: secret
    volumes:
      - db-data:/var/lib/postgresql/data

volumes:
  db-data:
```

运行：
```bash
docker-compose up -d
```

## 最佳实践

1. **使用轻量级基础镜像**：优先选择alpine版本
2. **多阶段构建**：减小最终镜像体积
3. **合理使用缓存**：将不常变化的层放在前面
4. **不要在容器中存储数据**：使用volumes持久化
5. **限制资源使用**：使用`--memory`和`--cpus`参数
6. **健康检查**：在Dockerfile中添加HEALTHCHECK指令

## 常见问题

### 容器无法访问
检查端口映射和防火墙设置：
```bash
docker port container_name
```

### 容器日志查看
```bash
docker logs -f container_name
```

### 进入运行中的容器
```bash
docker exec -it container_name /bin/sh
```

## 安全建议

- 不要以root用户运行容器
- 定期更新基础镜像
- 扫描镜像漏洞：`docker scan image_name`
- 使用secrets管理敏感信息
- 限制容器权限：使用`--read-only`等参数

## 监控与日志

### 资源使用统计
```bash
docker stats
```

### 日志驱动配置
```bash
docker run --log-driver=json-file --log-opt max-size=10m nginx
```

## 总结

Docker通过容器化技术简化了应用的部署和管理流程。掌握Docker的基本概念和命令，能够显著提升开发和运维效率。建议在实际项目中结合CI/CD流程，实现自动化部署。

## 参考资源

- [Docker官方文档](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Dockerfile最佳实践](https://docs.docker.com/develop/dev-best-practices/)
