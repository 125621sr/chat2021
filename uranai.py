import time
import random
import IPython
from google.colab import output

# アイコンの指定
BOT_ICON = 'https://1.bp.blogspot.com/-_tnyZ46sJ_M/X1LsmD2uZOI/AAAAAAABa_w/FjmL4ow5bQY91MTkM63t5h_ADylNvTfrgCNcBGAsYHQ/s180-c/yumekawa_angel_tenshi.png'
YOUR_ICON = 'https://1.bp.blogspot.com/-ggxynLSeNT0/XlygE7S-29I/AAAAAAABXs4/Mz9Vv5TvfhAP1SkHC3CEKq_gu7q1ofOfACNcBGAsYHQ/s180-c/yumekawa_baby.png'

# フレーム 状態をもつ辞書
# 'birthdaya', 'birthdayb', 'message','asking'
frame = {}

message = ['笑顔を見せると良いことあるかも！','恋が実りますように！！！応援してるよ💕💕','勇気を出して話しかけると良いことあるかも！!(UoxoU)♡','自分に自信を持つと幸せが増えるよ！自信もって大丈夫👍',
           'ポジティブに行こう👍👍','できることからコツコツ始めて行くだけでも良き✊','あなたが努力しているの知ってるから、大丈夫！！',
           '素敵なことが起こりますように…(=^・・^=)','2人の距離が縮まるおまじないをかけるね！えいっ🎵']

def uranai(input_text):
  global frame # 外部の状態を参照する
  if 'asking' in frame:  # asking から更新する
    frame[frame['asking']] = input_text.strip()
    del frame['asking']

  if 'birthdaya' not in frame:
    frame['asking'] = 'birthdaya' # 誕生日をたずねる  
    return 'あなたの誕生日は？'

  if 'birthdaya' in frame and 'birthdayb' not in frame:
    frame['asking'] = 'birthdayb' # 相手の誕生日をたずねる    
    return '相手の誕生日は？'


  if 'birthdaya' in frame and 'birthdayb' in frame and 'message' not in frame:
    
    frame['asking'] = 'message'

    birthdaya = frame['birthdaya']
    birthdayb = frame['birthdayb']


    while len(birthdaya) >= 2:
      birthdaya = str(sum(int(x) for x in birthdaya))
      if birthdaya in ('11','22','33','44'):
        break

    while len(birthdayb) >= 2:
      birthdayb = str(sum(int(x) for x in birthdayb))
      if birthdayb in ('11','22','33','44'):
        break

    x = abs(int(birthdaya)-int(birthdayb))

    y = (-100/43)*x+100

    if int(y)>=90:
      return '2人の相性はとても良いです 💗'
    if int(y)>=30 and int(y)<80:
      return '2人の相性は良いです 💛'
    if int(y)<30:
      return '2人の相性は普通かも 💦'

  if 'birthdaya' in frame and 'birthdayb' in frame and 'message' in frame:

    frame[frame['message']] = input_text.strip()
    del frame['message']

    return  random.choice(message)

  return output_text

def run_chat(chat = uranai, start='相性占いする？', **kw):

  def display_bot(bot_text):
    with output.redirect_to_element('#output'):
      bot_name = kw.get('bot_name', 'ボット')
      bot_icon = kw.get('bot_icon', BOT_ICON)
      display(IPython.display.HTML(f'''
      <div class="sb-box">
        <div class="icon-img icon-img-left">
            <img src="{bot_icon}" width="60px">
        </div><!-- /.icon-img icon-img-left -->
        <div class="icon-name icon-name-left">{bot_name}</div>
        <div class="sb-side sb-side-left">
            <div class="sb-txt sb-txt-left">
              {bot_text}
            </div><!-- /.sb-txt sb-txt-left -->
        </div><!-- /.sb-side sb-side-left -->
    </div><!-- /.sb-box -->
      '''))

  def display_you(your_text):
    with output.redirect_to_element('#output'):
      your_name = kw.get('your_name', 'あなた')
      your_icon = kw.get('your_icon', YOUR_ICON)

      display(IPython.display.HTML(f'''
      <div class="sb-box">
        <div class="icon-img icon-img-right">
            <img src="{your_icon}" width="60px">
        </div><!-- /.icon-img icon-img-right -->
        <div class="icon-name icon-name-right">{your_name}</div>
        <div class="sb-side sb-side-right">
            <div class="sb-txt sb-txt-right">
              {your_text}
            </div><!-- /.sb-txt sb-txt-right -->
        </div><!-- /.sb-side sb-side-right -->
      </div><!-- /.sb-box -->
      '''))

  display(IPython.display.HTML('''
      <style>
        /* 全体 */
        .sb-box {
            position: relative;
            overflow: hidden;
        }

        /* アイコン画像 */
        .icon-img {
            position: absolute;
            overflow: hidden;
            top: 0;
            width: 80px;
            height: 80px;
        }

        /* アイコン画像（左） */
        .icon-img-left {
            left: 0;
        }

        /* アイコン画像（右） */
        .icon-img-right {
            right: 0;
        }

        /* アイコン画像 */
        .icon-img img {
            border-radius: 50%;
        }

        /* アイコンネーム */
        .icon-name {
            position: absolute;
            width: 80px;
            text-align: center;
            top: 83px;
            color: mediumpurple;
            font-size: 10px;
        }

        /* アイコンネーム（左） */
        .icon-name-left {
            left: 0;
        }

        /* アイコンネーム（右） */
        .icon-name-right {
            right: 0;
        }

        /* 吹き出し */
        .sb-side {
            position: relative;
            float: left;
            margin: 0 105px 40px 105px;
        }

        .sb-side-right {
            float: right;
        }

        /* 吹き出し内のテキスト */
        .sb-txt {
            position: relative;
            border: 1px solid mediumpurple;
            border-radius: 6px;
            background: mistyrose;
            color: mediumpurple;
            font-size: 15px;
            line-height: 1.7;
            padding: 18px;
        }

        .sb-txt>p:last-of-type {
            padding-bottom: 0;
            margin-bottom: 0;
        }

        /* 吹き出しの三角 */
        .sb-txt:before {
            content: "";
            position: absolute;
            border-style: solid;
            top: 16px;
            z-index: 3;
        }

        .sb-txt:after {
            content: "";
            position: absolute;
            border-style: solid;
            top: 15px;
            z-index: 2;
        }

        /* 吹き出しの三角（左） */
        .sb-txt-left:before {
            left: -7px;
            border-width: 7px 10px 7px 0;
            border-color: transparent mediumpurple transparent transparent;
        }

        .sb-txt-left:after {
            left: -10px;
            border-width: 8px 10px 8px 0;
            border-color: transparent #eee transparent transparent;
        }

        /* 吹き出しの三角（右） */
        .sb-txt-right:before {
            right: -7px;
            border-width: 7px 0 7px 10px;
            border-color: transparent transparent transparent mediumpurple;
        }

        .sb-txt-right:after {
            right: -10px;
            border-width: 8px 0 8px 10px;
            border-color: transparent transparent transparent #eee;
        }

        /* 767px（iPad）以下 */

        @media (max-width: 767px) {

            .icon-img {
                width: 60px;
                height: 60px;
            }

            /* アイコンネーム */
            .icon-name {
                width: 60px;
                top: 62px;
                font-size: 9px;
            }

            /* 吹き出し（左） */
            .sb-side-left {
                margin: 0 0 30px 78px;
                /* 吹き出し（左）の上下左右の余白を狭く */
            }

            /* 吹き出し（右） */
            .sb-side-right {
                margin: 0 78px 30px 0;
                /* 吹き出し（右）の上下左右の余白を狭く */
            }

            /* 吹き出し内のテキスト */
            .sb-txt {
                padding: 12px;
                /* 吹き出し内の上下左右の余白を-6px */
            }
        }
    </style>
      <script>
        var inputPane = document.getElementById('input');
        inputPane.addEventListener('keydown', (e) => {
          if(e.keyCode == 13) {
            google.colab.kernel.invokeFunction('notebook.Convert', [inputPane.value], {});
            inputPane.value=''
          }
        });
      </script>
    <div id='output' style='background: lavender; border: 1px solid mediumpurple;'></div>
    <div style='text-align: right'><textarea id='input' style='width: 100%; background: mistyrose;'></textarea></div>
      '''))

  def convert(your_text):
    display_you(your_text)
    bot_text = chat(your_text, **kw)
    time.sleep(random.randint(0,4))
    display_bot(bot_text)

  output.register_callback('notebook.Convert', convert)
  if start is not None:
    display_bot(start)

run_chat(chat=uranai)
