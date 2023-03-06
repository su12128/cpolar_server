1.路径和跨域都会导致请求的jscss文件错误无法解析
    Failed to load module script: Expected a JavaScript module script but the server responded with a MIME type of "text/html". Strict MIME type checking is enforced for module scripts per HTML spec.
    Refused to apply style from 'http://127.0.0.1:81/assets/index-d47e4197.css' because its MIME type ('text/html') is not a supported stylesheet MIME type, and strict MIME checking is enabled.

    解决跨域：（https://blog.csdn.net/cz20191106196/article/details/124294310）
    
    pip install django-cors-headers
    跨域三步走：
    1.INSTALLED_APPS追加：'corsheaders',  # 跨域配置1
    2.MIDDLEWARE插入中间件，注意位置在SessionMiddleware和CommonMiddleware之间：'corsheaders.middleware.CorsMiddleware',#跨域中间件
    3.setting.py文件添加白名单（或直接允许所有：CORS_ORIGIN_ALLOW_ALL = True）：
        CORS_ALLOW_CREDENTIALS = True
        CORS_ORIGIN_ALLOW_ALL = True
        CORS_ALLOW_METHODS = (
            'DELETE',
            'GET',
            'OPTIONS',
            'PATCH',
            'POST',
            'PUT',
            'VIEW',
        )

        CORS_ALLOW_HEADERS = (
            'XMLHttpRequest',
            'X_FILENAME',
            'accept-encoding',
            'authorization',
            'content-type',
            'dnt',
            'origin',
            'user-agent',
            'x-csrftoken',
            'x-requested-with',
            'Pragma',
        )


js 和css 文件响应为text/plain 导致浏览器无法解析问题：
    settings.py文件末尾追加
    import mimetypes
    mimetypes.add_type('text/css', '.css')
    mimetypes.add_type('application/javascript', '.js')