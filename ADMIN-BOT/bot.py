import discord
from discord.ext import commands
import typing
import random
import time
import abc
import rog

client = discord.Client()
bot = commands.Bot(command_prefix='/')


@bot.command()
async def kd(ctx):
    await bot.change_presence(activity=discord.Game(name='稼働中'))

@bot.command()
async def ks(ctx):
    await bot.change_presence(activity=discord.Game(name='故障中'))

@bot.command()
async def ik(ctx):
    await bot.change_presence(activity=discord.Game(name='逝かれた'))

@bot.command()
async def ku(ctx):
    await bot.change_presence(activity=discord.Game(name='更新中'))
  
@bot.command()
async def kus(ctx):
    await bot.change_presence(activity=discord.Game(name='更新の準備中'))

@bot.command()
async def tt(ctx):
    await bot.change_presence(activity=discord.Game(name='テスト中'))

@bot.command()
async def de(ctx):
    await bot.change_presence(activity=discord.Game(name='デバッグ中落ちる可能性あり'))

@bot.command()
async def no(ctx):
    await bot.change_presence(activity=None)

@bot.command()
async def s(ctx):
    for s in client.guilds:
        print(s)


@bot.event
async def on_message(message):  
    for word in rog.list:
      if message.author.bot:
        return
      if word in message.content:
        await message.delete()
        embed=discord.Embed(title="現在のコメントは削除されました",description=message.author.mention, color=0xdc0909)
        embed.add_field(name="削除されたコメント(部分):", value= word, inline=True)
        embed.add_field(name="理由：", value="現在のコメントは暴言にあたります", inline=True)
        embed.add_field(name="削除されたコメント(全文):", value= message.content, inline=False)  
        embed.add_field(name="違反したサーバー", value= message.guild, inline=True)
        embed.add_field(name="違反したチャンネル", value= message.channel, inline=True)
        embed.add_field(name="その他", value="意図しないで削除された場合浜で管理者までお願いします", inline=False)
        embed.add_field(name="違反した時間（UTC時間です日本時間は+９時間", value= message.created_at, inline=True)
                                                      

        await message.channel.send(embed=embed)
    await bot.process_commands(message)




       




class MemberRoles(commands.MemberConverter):
    async def convert(self, ctx, argument):
        member = await super().convert(ctx, argument)
        return [role.name for role in member.roles[1:]] # Remove everyone role!

@bot.command()
async def r(ctx, *, member: MemberRoles ):
    """Tells you a member's roles."""
    await ctx.send('ロール: ' + ', '.join(member))

@r.error
async def r_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('IDが間違っている可能性があります\nやり直してください')

@bot.command()
async def t(ctx, a: int, b: int):
    await ctx.send(a+b)
@t.error
async def t_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('数字・空白がない可能性があります\nやり直してください')

@bot.command()
async def h(ctx, a: int, b: int):
    await ctx.send(a-b)
@h.error
async def h_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('数字・空白がない可能性があります\nやり直してください')

@bot.command()
async def k(ctx, a: int, b: int):
    await ctx.send(a*b)

@k.error
async def k_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('数字・空白がない可能性があります\nやり直してください')

@bot.command()
async def w(ctx, a: int, b: int):
    await ctx.send(a/b)

@w.error
async def w_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('数字・空白がない可能性があります\nやり直してください')



@bot.command()
async def j(ctx, *, member: discord.Member):
    await ctx.send('{0} 入室履歴: {0.joined_at}' .format(member))

@j.error
async def j_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('IDが間違っている可能性があります\nやり直してくさい')

@bot.command()
async def d(ctx):
    await ctx.send("ダイスをスタートします最初に1000渡します")   

    num_random = random.randrange(-1000,+1000)
    m = int(num_random)
    if 1000> m> 0:
        time.sleep(2)
        await ctx.send(m)
        await ctx.send(m+1000)

        await ctx.send('やりましたね～～さぁ次も・・・')
        await ctx.send('再び実行する際は/dをお願いします')

        
    else:
        time.sleep(2)
        await ctx.send(m)
        await ctx.send(m-1000)

        await ctx.send('うーーん次がありますよ')
        await ctx.send('再び実行する際は/dをお願いします')

#さいしょに1000渡してそれを定義そこから1000-ｍでとれるかも・・・・/dしたら1000渡してスタートawaitで1000-ｍでおｋ・・・？

@bot.command()
async def em(ctx, a, b, c, d):
    embed=discord.Embed(title= a,description= b, color=0xdc0909)
    embed.add_field(name= c, value= d, inline=True)
    await ctx.send(embed=embed)

@em.error
async def em_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('空白がない可能性があります\nやり直してください')


    
@bot.command()
async def he(ctx):
    embed=discord.Embed(title=" 管理BOTのヘルプです",description= "コマンドの説明", color=0xdc0909)
    embed.add_field(name= "```/help```", value= "これです", inline=False)
    embed.add_field(name= "```/r [ユーザーID]```", value= "ユーザーのIDをいれてこの指定したIDについているロールを表示します", inline=False)
    embed.add_field(name= "```/j [ユーザーID]```", value= "ユーザーのIDをいれてこの指定したIDがこのサーバーに入室した日時を表示します", inline=False)
    embed.add_field(name= "```/em [タイトル] [サブタイトル]　[コメント1] [コメント2]```", value= "埋め込みで表示されます", inline=False)
    embed.add_field(name= "```/d```", value= "ダイスです暇なときどうぞ", inline=False)
 
    embed.add_field(name= "```/k [足される数] [足す数]```", value= "足し算ができます", inline=False)
    embed.add_field(name= "```/h [引かれる数] [引く数]```", value= "引き算ができます", inline=False)
    embed.add_field(name= "```/k [掛ける数] [掛けられる数]```", value= "掛け算ができます", inline=False)
    embed.add_field(name= "```/w [割られる数] [割る数]```", value= "割り算ができます", inline=False)
    embed.add_field(name= "告知", value= "特になし", inline=False)




      
    await ctx.send(embed=embed)







           
bot.run("トークン")

