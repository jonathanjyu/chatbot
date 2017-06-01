from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == 'begin'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == '2'

    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == '3'

    def is_going_to_state4(self, update):
        text = update.message.text
        return text.lower() == '4'

    def is_going_to_state5(self, update):
        text = update.message.text
        return text.lower() == '5'

    def is_going_to_state6(self, update):
        text = update.message.text
        return text.lower() == '6'

    def is_going_to_state7(self, update):
        text = update.message.text
        return text.lower() == '7'

    def is_going_to_state8(self, update):
        text = update.message.text
        return text.lower() == '8'

    def is_going_to_state9(self, update):
        text = update.message.text
        return text.lower() == '9'

    def is_going_to_state10(self, update):
        text = update.message.text
        return text.lower() == '10'

    def is_going_to_state11(self, update):
        text = update.message.text
        return text.lower() == '11'

    def is_going_to_state12(self, update):
        text = update.message.text
        return text.lower() == '12'

    def is_going_to_state13(self, update):
        text = update.message.text
        return text.lower() == '13'

    def is_going_to_state14(self, update):
        text = update.message.text
        return text.lower() == '14'

    def is_going_to_state15(self, update):
        text = update.message.text
        return text.lower() == '15'

    def is_going_to_stateA(self, update):
        text = update.message.text
        return text.lower() == 'a'

    def is_going_to_stateB(self, update):
        text = update.message.text
        return text.lower() == 'b'

    def is_going_to_stateC(self, update):
        text = update.message.text
        return text.lower() == 'c'

    def on_enter_state1(self, update):
        update.message.reply_text("愛人送的戒指不見了你認為是什麼原因? \n覺得是自己不小心__2\n認為是不好的先兆__3")
        #self.go_back(update)

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state2(self, update):
        update.message.reply_text("你曾經有過和對方第一次見面,就有似曾相識的感覺嗎?\n有__3\n沒有或不記得了__4")
        #self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')


    def on_enter_state3(self, update):
        update.message.reply_text("你注意到某個明星,正好是你喜歡的型,看到他/她會心跳加速嗎?\n會__4\n不會__5")
        #self.go_back(update)

    def on_exit_state3(self, update):
        print('Leaving state3')

    def on_enter_state4(self, update):
        update.message.reply_text("喜歡的電影,不管看幾次都不會厭煩,而且一樣會被感動嗎?\n會__5\n不會__6")
        #self.go_back(update)

    def on_exit_state4(self, update):
        print('Leaving state4')

    def on_enter_state5(self, update):
        update.message.reply_text("買東西時,看到很喜歡的東西,雖然不是一定要買的必需品,卻常將它買下來?\n會__6\n不會__7")
        #self.go_back(update)

    def on_exit_state5(self, update):
        print('Leaving state5')

    def on_enter_state6(self, update):
        update.message.reply_text("不管是好事或壞事,你認為自己的預感相當靈驗嗎?\n是__7\n不是__8")
        #self.go_back(update)

    def on_exit_state6(self, update):
        print('Leaving state6')

    def on_enter_state7(self, update):
        update.message.reply_text("喜歡上對方的原因通常是哪一種?\n對方的外型__8\n彼此能合得來__9")
        #self.go_back(update)

    def on_exit_state7(self, update):
        print('Leaving state7')

    def on_enter_state8(self, update):
        update.message.reply_text("你會羨慕哪一種情侶?\n沒見面時一定會和對方通電話__9\n從來都不吵架的一對__10")
        #self.go_back(update)

    def on_exit_state8(self, update):
        print('Leaving state8')

    def on_enter_state9(self, update):
        update.message.reply_text("在街上遇到老同學,會怎麼想?\n只是偶然,沒什麼大不了__10\n不可思議,一定是緣份的安排__11")
        #self.go_back(update)

    def on_exit_state9(self, update):
        print('Leaving state9')

    def on_enter_state10(self, update):
        update.message.reply_text("哪件事讓你覺得冥冥中有人在主宰?\n和對方同一天生日__11\n曾經在外地遇到的陌生人,突然又在附近碰面__12")
        #self.go_back(update)

    def on_exit_state10(self, update):
        print('Leaving state10')

    def on_enter_state11(self, update):
        update.message.reply_text("一對真正相愛的戀人,是不需要言語就可以了解對方的心意,你也想遇到這種情人嗎?\n想__12\n不想__13")
        #self.go_back(update)

    def on_exit_state11(self, update):
        print('Leaving state11')

    def on_enter_state12(self, update):
        update.message.reply_text("你認為如何才能和夢中情人相遇?\n自己要去多製造機會__13\n一切聽天由命__14")
        #self.go_back(update)

    def on_exit_state12(self, update):
        print('Leaving state12')

    def on_enter_state13(self, update):
        update.message.reply_text("你認為相信命中注定的人都一定是悲劇收場嗎?\n認同__14\n不認同__15")
        #self.go_back(update)

    def on_exit_state13(self, update):
        print('Leaving state13')

    def on_enter_state14(self, update):
        update.message.reply_text("認為人生就是為了和有人緣的人相遇,就算失戀也是一種很值得的回憶?\n認同__B\n不認同__A")
        #self.go_back(update)

    def on_exit_state14(self, update):
        print('Leaving state14')

    def on_enter_state15(self, update):
        update.message.reply_text("和喜歡的人交往後,你會變得如何?\n什麼事都要跟對方一起做__B\n變得魂不守舍__C")
        #self.go_back(update)

    def on_exit_state15(self, update):
        print('Leaving state15')

    def on_enter_stateA(self, update):
        update.message.reply_text("A:總是愛「戀到最高點」的浪漫派!\n非常相信這世界上有愛情的紅線,是個無可救藥的浪漫主意者.不過如果在現實生活中,出現的人不是你所謂的「命中注定的人」你就會放棄對方.而繼續等待「那份感覺」,那份「前世註定的因緣」殊不知太過執著可能會浪費你的青春,也浪費掉很多機會.不要再迷信下去了!好好留意身邊的人吧!")
        self.go_back(update)

    def on_exit_stateA(self, update):
        print('Leaving stateA')

    def on_enter_stateB(self, update):
        update.message.reply_text("B:愛情的硬漢!完全不相信命運\n認為「命運」這兩個字很苦命,這樣的你從不知浪漫是什麼,也不相信一見鍾情.戀愛的機會也就很難降臨到你頭上.所以,首先你必須先好好的了解自己,到底想要怎麼樣的戀情,想像一下愛情的樣子,想像一下對方的樣子,再不然就多看浪漫經典的愛情電影,勾勒出理想中真愛的樣子,說不定這樣就能夠找到戀愛的「感覺」.")
        self.go_back(update)

    def on_exit_stateB(self, update):
        print('Leaving stateB')

    def on_enter_stateC(self, update):
        update.message.reply_text("C:堅定的愛情戰士!\n你相信有「月下老人」,但也認為命運可以自己去創造.當你喜歡上一個人後,心裡便再也容不下第二個人.這樣的你從不會被傳說中的一見鍾情或什麼前生註定的浪漫說詞所迷惑,你會把握並珍惜眼前的人.")
        self.go_back(update)

    def on_exit_stateC(self, update):
        print('Leaving stateC')
