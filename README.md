# 网易云音乐无损解析


**功能强大的网易云音乐解析工具**

支持歌曲搜索 | 单曲解析 | 歌单解析 | 专辑解析 | 音乐下载

[使用文档](./使用文档.md)

</div>

---

> **⚠️ 重要声明**  
> 本项目采用 MIT 许可证开源。根据 MIT 许可证的条款，任何个人或组织均可自由使用、修改和分发本项目的源代码，包括用于商业项目。

**注意**：本项目旨在为开源社区做贡献，我们鼓励用户：
- 在遵守开源精神的前提下使用和分享代码
- 如有改进，欢迎贡献回本项目
- 在商业使用中，请考虑对开源项目的支持和回馈

虽然 MIT 许可证允许商业使用，但我们希望用户能尊重开源精神，合理使用本项目。

## ✨ 功能特性

### 🎵 核心功能
- **🔍 智能检索与解析**：支持关键词搜索、单曲、歌单、专辑的深度解析。
- **⬇️ 多资源下盘**：直接获取最高达 `Hi-Res` 与 `超清母带` 的音频直链与下载。
- **🎨 丝滑响应式 UI**：引入仿原生毛玻璃（Glassmorphism）设计，支持**单点切换及跟随系统的暗黑/浅色自适应主题**，并在导航栏增设了**独立的高端「设置」控制面板**。
- **� 双语歌词元信息**：下载的音乐文件不仅自动注入高清封面封面，还支持对**原生语言及中文翻译进行完美对齐融合**，写入标准歌词标签中。
- **⚙️ 无感自动化清理**：内置后端定时文件大扫除机制，拒绝临时文件撑爆服务器硬盘。

### 🎼 音质支持
- `standard`：标准音质 (128kbps)
- `exhigh`：极高音质 (320kbps)
- `lossless`：无损音质 (FLAC)
- `hires`：Hi-Res音质 (24bit/96kHz)
- `jyeffect`：高清环绕声
- `sky`：沉浸环绕声
- `jymaster`：超清母带

### 🌐 使用方式
- **Web界面**：直观友好的网页操作界面
- **RESTful API**：完整的API接口支持
- **批量处理**：支持歌单和专辑的批量解析
- **多格式支持**：支持ID和链接多种输入格式

---

## 🚀 快速开始

### 环境要求
- Python 3.7+
- 网易云音乐黑胶会员账号

### 安装步骤

#### 1. 克隆项目
```bash
git clone https://github.com/Suxiaoqinx/Netease_url.git
cd Netease_url
```

#### 2. 安装依赖
```bash
pip install -r requirements.txt
```

#### 3. 配置Cookie
在 `cookie.txt` 文件中填入黑胶会员账号的Cookie：

> 💡 **获取Cookie方法**：登录网易云音乐网页版 → F12开发者工具 → Network标签页 → 复制任意请求的Cookie值

#### 4. 启动服务
```bash
python main.py
```

#### 5. 访问界面
打开浏览器访问：`http://localhost:5000`

### 🐳 Docker部署

```bash
# 使用Docker Compose
docker-compose up -d

# 或使用Docker
docker build -t netease_url_for_nas .
docker run -d -p 5000:5000 netease_url_for_nas
```

---

## 📖 使用指南

### Web界面使用

#### 🔍 歌曲搜索
1. 选择功能：**歌曲搜索**
2. 输入关键词（歌曲名、歌手名等）
3. 点击**搜索**按钮
4. 在搜索结果中点击**解析**或**下载**按钮

#### 🎧 单曲解析
1. 选择功能：**单曲解析**
2. 输入歌曲ID或网易云音乐链接
   - 支持格式：`1234567890` 或 `https://music.163.com/song?id=1234567890`
3. 点击**解析**按钮查看歌曲信息

#### 📋 歌单解析
1. 选择功能：**歌单解析**
2. 输入歌单ID或网易云音乐歌单链接
   - 支持格式：`1234567890` 或 `https://music.163.com/playlist?id=1234567890`
3. 点击**解析**按钮查看歌单中所有歌曲
4. 点击单首歌曲的**解析**或**下载**按钮

#### 💿 专辑解析
1. 选择功能：**专辑解析**
2. 输入专辑ID或网易云音乐专辑链接
   - 支持格式：`1234567890` 或 `https://music.163.com/album?id=1234567890`
3. 点击**解析**按钮查看专辑中所有歌曲
4. 点击单首歌曲的**解析**或**下载**按钮

#### ⬇️ 音乐下载
1. 选择功能：**单曲/歌单/专辑**
2. 搜索或输入相关ID/链接
3. 选择您所需要的目标音质（例如：无损或沉浸环绕声）
4. 直接点击**解析**，并在卡片后点击**直接下载**按钮获取文件，歌单/专辑支持一键下载全集。

#### ⚙️ 高级参数设置
在顶部导航最右侧的 **设置** 面板中，您可以按需自由调配：
- **搜索上限限制**：范围 1-100（过高可能被 API 服务器限流）。
- **文件重命名规则**：自定义下载生成的音频标头风格。
- **自动化大扫除**：设定存活时长后，服务端会在后台优雅静默地清除滞留临时文件。
- **推流分离模式**：开启“推流下载至浏览器”将让音乐保存至您当前的设备；若关闭，音乐只会悄悄存储在服务器磁盘供进阶分发（防黑客直接爬取）。

### 支持的链接格式

```
# 歌曲链接
https://music.163.com/song?id=1234567890
https://music.163.com/#/song?id=1234567890

# 歌单链接
https://music.163.com/playlist?id=1234567890
https://music.163.com/#/playlist?id=1234567890

# 专辑链接
https://music.163.com/album?id=1234567890
https://music.163.com/#/album?id=1234567890

# 直接使用ID
1234567890
```

## 🔌 API接口文档

### 基础信息
- **Base URL**: `http://localhost:5000`
- **请求方式**: GET / POST
- **响应格式**: JSON

### 接口列表

#### 1. 健康检查
```http
GET /health
```
**响应示例**:
```json
{
  "status": "ok",
  "message": "Service is running"
}
```

#### 2. 歌曲搜索
```http
POST /search
Content-Type: application/json

{
  "keywords": "周杰伦 稻香",
  "limit": 10
}
```
**响应示例**:
```json
{
  "code": 200,
  "result": {
    "songs": [
      {
        "id": 185668,
        "name": "稻香",
        "artists": ["周杰伦"],
        "album": "魔杰座",
        "duration": 223000
      }
    ]
  }
}
```

#### 3. 单曲解析
```http
POST /song
Content-Type: application/json

{
  "id": "185668"
}
```

#### 4. 歌单解析
```http
POST /playlist
Content-Type: application/json

{
  "id": "123456789"
}
```

#### 5. 专辑解析
```http
POST /album
Content-Type: application/json

{
  "id": "123456789"
}
```

#### 6. 音乐下载
```http
POST /download
Content-Type: application/json

{
  "id": "185668",
  "quality": "lossless"
}
```
**响应**: 直接返回音频文件流

---

## 音质参数说明（仅限单曲解析）

- `standard`：标准音质
- `exhigh`：极高音质
- `lossless`：无损音质
- `hires`：Hi-Res音质
- `jyeffect`：高清环绕声
- `sky`：沉浸环绕声
- `jymaster`：超清母带

> 黑胶VIP音质：standard, exhigh, lossless, hires, jyeffect  
> 黑胶SVIP音质：sky, jymaster

---

## Docker 一键部署

本项目已针对容器化环境进行了**深度瘦身与安全优化（基于 Alpine & Python 3.11）**。

1. **环境配置与修改**
   - 如需修改映射端口，请编辑 `.env` 或 `docker-compose.yml` 文件中的 `ports` 配置，例如：
     ```yaml
     ports:
       - "8080:5000"
     ```

2. **启动极速构建与服务**
   ```bash
   docker-compose up -d --build
   ```


---

## 注意事项

- 必须使用黑胶会员账号的 Cookie 才能解析高音质资源。
- Cookie 格式请严格按照 `cookie.txt` 示例填写。

---

## 致谢

- [Ravizhan](https://github.com/Suxiaoqinx/Netease_url)

---


欢迎 Star、Fork 和 PR！




