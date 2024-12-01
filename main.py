from flet import *
def main(page:Page):
    ########window pro======
    page.title=("Ismail")
    page.window.height = 740
    page.window.width= 390
    page.window.top = 10
    page.window.left = 960
    page.theme_mode = ThemeMode.LIGHT

    def route_change(route):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(
                        title= Text("Ismail flet"),
                        color= 'white',
                        #bgcolor=colors.PURPLE
                        ),
                    Text('Welcom...', size=24, color='black', width=370, text_align='center'),
                    Row([
                        Image(src="", width=200)

                    ],alignment=MainAxisAlignment.CENTER),
                    Text("اهلا وسهلا بكم في تطبيقنا", size=15, color='purple', width=350, text_align='center'),
                    Row([
                        ElevatedButton(
                            "الدخول للحساب",
                            width=150,
                            style=ButtonStyle(bgcolor='purple', color='white'),
                            on_click=lambda _: page.go("/login")
                            ),
                        
                        ElevatedButton(
                            "انشاء الحساب",
                            width=150,
                            style=ButtonStyle(bgcolor='purple', color='white'),
                            on_click=lambda _: page.go("/signup")
                            ),
                        #ElevatedButton("انشاء للحساب", on_click=lambda _: page.go("/signup"))
                       ],alignment=MainAxisAlignment.CENTER),
                    
                ],
                )
        )
        if page.route == "/login":
            page.views.append(
            View(
                "/login",
                [
                    AppBar(
                        title= Text("Login System"),
                        color= 'white',
                        bgcolor=colors.PURPLE
                        ),
                    Text('تسجيل الدخول', size=24, color='black', width=370, text_align='center'),
                    TextField(label='Email: البريد'),
                    TextField(label='Password : كلمة المرور'),
                    Row([
                        ElevatedButton(
                            "الدخول الان",
                            width=150,
                            style=ButtonStyle(bgcolor='purple', color='white'),                           
                            ),
                        
                        ElevatedButton(
                            "حساب جديد",
                            width=150,
                            style=ButtonStyle(bgcolor='purple', color='white'),
                            on_click=lambda _: page.go("/signup")
                            ),                      
                       ],alignment=MainAxisAlignment.CENTER),
                   
                ],
                )
        )
        
        
        if page.route == "/signup":
            page.views.append(
            View(
                "/signup",
                [
                    AppBar(
                        title= Text("signup System"),
                        color= 'white',
                        #bgcolor=colors.WHITE
                        ),
                    Text('انشاء حساب جديد', size=24, color='black', width=370, text_align='center'),
                    TextField(label='Email: البريد'),
                    TextField(label='Full name :الاسم الكامل'),
                    TextField(label='Password : كلمة المرور'),
                    TextField(label='Password: اعادة كلمة المرور'),
                    Row([
                        ElevatedButton(
                            "انشاء حساب",
                            width=150,
                            style=ButtonStyle(bgcolor='purple', color='white'),                           
                            ),
                        
                        ElevatedButton(
                            "لديك حساب بالفعل",
                            width=150,
                            style=ButtonStyle(bgcolor='purple', color='white'),
                            on_click=lambda _: page.go("/login")
                            ),                      
                       ],alignment=MainAxisAlignment.CENTER),
                    
                ],
                )
        )

        page.update()
    
    def page_go(view):
        page.views.pop()
        back_page =page.views[-1]
        page.go(back_page.route)
    page.on_route_change = route_change
    page.on_view_pop = page_go
    page.go(page.route)
app(main)
