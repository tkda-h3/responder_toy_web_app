import responder
from responder import Request, Response

api = responder.API()


@api.route('/hello/{who}/html')
async def hello(req: Request, resp: Response, *, who: str):
    # templatesディレクトリに配置
    resp.html = api.template('hello.html', who=who)

    # local()[f'HTTP_{number}'] = number の形で定数を作成しているので補完が効かない
    print(api.status_codes.HTTP_200)


if __name__ == '__main__':
    api.run()

