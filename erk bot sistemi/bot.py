import discord
from discord import app_commands
from discord.ext import commands, tasks
import pymongo
from config import *
import datetime
import locale
import pytz
import asyncio
from discord.ui import Button, View
import random
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
intents.messages = True
intents.members = True
intents.voice_states = True
intents.guilds = True
locale.setlocale(locale.LC_ALL, 'turkish') 

#--------------------------------------------------------------------------------------------------------------------------

token = "MTE2NTIxMTAzNDEwMjAyMjI5Ng.GJ445_.M9dpfVPx9p11bOTh3AsbPfBipEf_BziYwY8tuM" # Bot token'i
url = "mongodb+srv://ozberk:0808er11@cluster0.hwi4pdb.mongodb.net/?retryWrites=true&w=majority" # MongoDB url
prefix = "!" #bot prefixi
yonetici_id = 1245799328438812672 #yönetici rol id
kayit_yetkili = 1245799328438812672 #kayıt yetkili rol id
kayitsiz_rol_id = 1245799328438812672 #kayıtsız rol id
erkek_rol_id = 1245799328438812672 #erkek rol id
kiz_rol_id = 1245799328438812672 #kız rol id
supheli_rol_id = 1245799328438812672 #şüpheli rol id
hg_kanal_id = 1245797056321294359 #hos geldin kanal id
bb_kanal_id = 1245797056321294359 #gidenler kanal id
log_kanal_id = 1245797056321294359 #log kanal id
bl_log_kanal_id = 1245797056321294359 #blacklist log kanal id
data_log_kanal_id = 1245797056321294359 #data işlemleri için log kanal id
kurallar_kanal_id = 1245797056321294359 #kurallar kanal id
kayit_kanal_id = 1245797056321294359 #kayıt kanal id
genel_chat_id = 1245797056321294359 #genel chat kanal id
supheli_kanal_id = 1245797056321294359 #şüpheli log kanal id
sesli_kayit_kanal_id = 1245797056321294360 #Sesli kayıt kanal id
supheli_hesap_suresi = 30 #hesap süre yazan günden kısa ise şüpheliye atar
min_age = 13 # üye kayıtı için minimum yaş sınırı
footer = "Hata ve Sorun Ulaşımı için KASADİOVALE#0001" # footer ve oynuyor kısmı

#------------------------------------------------------------------------------------------------------------------------------

client = pymongo.MongoClient(url)
db = client['user_data']
db = client['para']  # Veritabanı adını belirtin
para_collection = db['banka']  # Para verilerini saklayacağınız koleksiyonu seçin
db = client['rp'] # rp depo vt si
rp_collection = db['kelime_sayisi'] # RP kelime sayısı verilerini saklayacağınız koleksiyonu seçin


bot = commands.Bot(command_prefix=prefix, intents=intents)


@bot.command()
async def kayıtbilgi(ctx):
    # İlk olarak HOŞGELDİN mesajını içeren bir embed oluşturulur.
    embed = discord.Embed(title="HOŞGELDİN", color=0x8A2BE2)  # Mor renk: 0x8A2BE2
    embed.add_field(name="1. Soru", value="Harry Potter biliyor musunuz?", inline=False)
    await ctx.send(embed=embed)

    # Kullanıcının cevabını beklemek için bir kontrol fonksiyonu tanımlanır.
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        # Kullanıcının cevabı beklenir, maksimum bekleme süresi 60 saniyedir.
        msg = await bot.wait_for('message', timeout=60, check=check)
        
        if msg.content.lower() in ['evet', 'biliyorum']:
            # Eğer kullanıcı evet veya biliyorum cevabını verirse, bir sonraki soruya geçilir.
            embed = discord.Embed(title="2. Soru", color=0x8A2BE2)
            embed.add_field(name="Sonraki Soru", value="Rol yapmayı biliyor musunuz?", inline=False)
            await ctx.send(embed=embed)
            
            # Kullanıcının ikinci soruya cevabını beklenir.
            msg = await bot.wait_for('message', timeout=60, check=check)
            if msg.content.lower() in ['hayır', 'bilmiyorum']:
                # Eğer kullanıcı hayır veya bilmiyorum cevabını verirse, öğrenmesi gerektiğini belirten mesaj gönderilir.
                embed = discord.Embed(title="Üzgünüm, Rol yapmayı öğrenmelisiniz", description="En yakın zamanda ders alınız!", color=0x8A2BE2)
                await ctx.send(embed=embed)
                
            else:
                # Kullanıcı evet veya biliyorum cevabını verirse, bilgilendirme mesajı gönderilir.
                embed = discord.Embed(title="Sunucu Sistemi", description="Sunucumuzda ders sistemi şöyle 11-15 yani 1.sınıf ile 5.sınıf arasında istediğin derse girebiliyorsun ama 16 yaşında yani 6.sınıf olduğunda bölüm seçiyorsun, Profesörlük yada bakanlık tarzı, Seni etiketlediğim bir yer olacak(evren büyüleri kanalına etiketleyeceksin), Orada listeli olanlar !büyü avadakedavra gibi kulkanılıyor. Listesiz alfabetik olan ise Hem ne işe yaradıkları hem listede olmayanlar. İki çeşit zar var. !düello ve !zar, !düello şu Karşılıklı düelloda kullanılıyor, normal zar ise eylem zarı birine tokat atmak gibi amaçlarda kullanılıyor. Birde rol sayacı var, Kelime başı 5 galleon. Birde İki banka var biri rol içi diğeri rol dışı bir tanesi rol bilgilendirmede, rol dışında olanda sadece para bakılıyor, rol içinde olanda ise yani diagon yolundakinde, para çekiyorsunuz ama rol yazarak, Sonra ürünler yetenekler var. Hem tl hem galleon ile. Birde ev sistemi var, Villayı 2 haftada bir 5k galleon vererek kiralıyorsun yada 50k vererek satın alıyorsun.", color=0x8A2BE2)
                await ctx.send(embed=embed)
            
        else:
            # Kullanıcı evet veya biliyorum cevabını vermezse, özür mesajı gönderilir.
            embed = discord.Embed(title="Üzgünüm, olmadı. Bilmek önemli!", description="Harry Potter öğrenmelisiniz!", color=0x8A2BE2)
            await ctx.send(embed=embed)
    except asyncio.TimeoutError:
        # Belirlenen süre içerisinde kullanıcı cevap vermezse, zaman aşımı mesajı gönderilir.
        await ctx.send("Zaman aşımına uğradı.")


@bot.command(name="bina")
async def bina(ctx):
    embed = discord.Embed(
        title="Hangi binada olmak istersin, neylere önem verirsin?",
        description="Örnek olarak:\n1- Cesaretli misin, sadakatli misin ve kahramanlık yapmayı düşünür müsün?\n2- Hırslı, azimli ve asil misin?\n3- Çalışmaya, eşitliğe ve adalete değer verir misin?\n4- Akıllı, bilgili ve erdemli misin?",
        color=discord.Color.blue()
    )
    embed.set_footer(text="Lütfen aşağıdaki butonlardan birine tıklayarak seçiminizi yapın.")

    message = await ctx.send(embed=embed)

    # Butonları ekleyelim
    await message.add_reaction("1️⃣")
    await message.add_reaction("2️⃣")
    await message.add_reaction("3️⃣")
    await message.add_reaction("4️⃣")

@bot.event
async def on_raw_reaction_add(payload):
    if payload.user_id != bot.user.id:
        message_id = payload.message_id
        channel = bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(message_id)
        member = channel.guild.get_member(payload.user_id)
        if message.author == bot.user:
            emoji = str(payload.emoji)
            if emoji == "1️⃣":
                embed = discord.Embed(
                    title="Gryffindor",
                    description=f"{member.mention}, seni Gryffindor'a yollarım belki\nZamanla olursun aslanın teki,\nYiğittir orada kalan çocuklar,\nHepsinin yüreği, nah, mangal kadar.",
                    color=discord.Color.red()
                )
                embed.set_footer(text="Cesaretli, sadakatli ve kahraman olabilecek biri olarak aramıza katıldın, hoşgeldin!")
                embed.set_image(url="https://media.tenor.com/mbb_vsQMsVoAAAAC/gryffindor-harrypotter.gif")
                await message.reply(embed=embed)

            elif emoji == "2️⃣":
                embed = discord.Embed(
                    title="Slytherin",
                    description=f"{member.mention}, düşersin belki de Slytherin'e sen,\nBir başkadır sanki oraya giden,\nAmaçları için neler yapmazlar\nAçıklasam bitmez sabaha kadar.",
                    color=discord.Color.green()
                )
                embed.set_footer(text="Hırslı, azimli ve asil biri olarak aramıza katılmaya hak kazandın!")
                embed.set_image(url="https://media.tenor.com/xUbaOIunGp4AAAAC/slytherin-hp.gif")
                await message.reply(embed=embed)

            elif emoji == "3️⃣":
                embed = discord.Embed(
                    title="Hufflepuff",
                    description=f"{member.mention}, belki de düşersin Hufflepuff'a\nHaksızlığı hemen kaldırıp rafa\nAdalet uğruna savaş verirsin\nHer yere mutluluk götürmek için.",
                    color=discord.Color.gold()
                )
                embed.set_footer(text="Çalışkan, eşitlikçi ve adaletsizliğe göz yummayan biri olduğun için aramızdasın, hoşgeldin!")
                embed.set_image(url="https://media.tenor.com/UAs0m2U91tUAAAAC/hufflepuff.gif")
                await message.reply(embed=embed)

            elif emoji == "4️⃣":
                embed = discord.Embed(
                    title="Ravenclaw",
                    description=f"{member.mention}, Ravenclaw kısmetin belki,\nOradakilerin hiç çıkmaz sesi,\nMantıktır onlarca önemli olan,\nÖyle kurtulurlar tüm sorunladan.",
                    color=discord.Color.blue()
                )
                embed.set_footer(text="Akıllı, bilgili ve erdemli birisin, aramıza hoşgeldin!")
                embed.set_image(url="https://media.tenor.com/Sgm7TzrEQzAAAAAC/harry-potter-ravenclaw.gif")
                await message.reply(embed=embed)


class RPListPaginator:
    def __init__(self, ctx, records):
        self.ctx = ctx
        self.records = records
        self.page = 1

    async def send_page(self):
        start_index = (self.page - 1) * 5
        end_index = self.page * 5
        total_pages = (len(self.records) + 4) // 5  # İleri ve geri butonlarını belirlemek için

        embed = discord.Embed(title="Kelime Sayısı Listesi", color=discord.Color.red())
        for rank, record in enumerate(self.records[start_index:end_index], start=start_index + 1):
            embed.add_field(name=f"{rank}. {record['user_name']}", value=f"{record['word_count']} kelime", inline=False)

        embed.set_footer(text=f"Sayfa {self.page}/{total_pages}")

        if self.page < total_pages:
            embed.set_author(name="İleri için sonraki sayfa emojisi ile tepki verin.")
        if self.page > 1:
            embed.set_author(name="Geri için önceki sayfa emojisi ile tepki verin.")

        message = await self.ctx.send(embed=embed)

        if self.page < total_pages:
            await message.add_reaction("⏭️")
        if self.page > 1:
            await message.add_reaction("⏮️")

        def check(reaction, user):
            return user == self.ctx.author and str(reaction.emoji) in ["⏭️", "⏮️"]

        try:
            reaction, user = await bot.wait_for("reaction_add", timeout=60, check=check)

            if str(reaction.emoji) == "⏭️" and self.page < total_pages:
                self.page += 1
            elif str(reaction.emoji) == "⏮️" and self.page > 1:
                self.page -= 1

            await message.delete()
            await self.send_page()
        except asyncio.TimeoutError:
            await message.clear_reactions()

@bot.command()
async def rplist(ctx):
    records = list(rp_collection.find().sort("word_count", pymongo.DESCENDING))
    if not records:
        await ctx.send("Kayıtlı kullanıcı bulunamadı.")
        return

    paginator = RPListPaginator(ctx, records)
    await paginator.send_page()

@bot.command()
async def kelimesıfırla(ctx):
    # Tüm kayıtların kelime sayısını sıfırla
    rp_collection.update_many({}, {"$set": {"word_count": 0}})
    await ctx.send("Tüm kelime sayıları sıfırlandı.")


@bot.command()
async def enson(ctx):
    async for message in ctx.channel.history(before=ctx.message.created_at):
        if message.author == ctx.author:
            embed = discord.Embed(
                title="Önceki Mesaj",
                color=discord.Color.red(),
                timestamp=message.created_at
            )
            embed.set_author(name=ctx.author.display_name)
            embed.add_field(name="Kanal", value=message.channel.mention, inline=False)
            embed.add_field(name="İçerik", value=message.content, inline=False)
            embed.add_field(name="Tarih", value=message.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
            await ctx.send(embed=embed)
            return
    else:
        await ctx.send("Önceki bir mesajınız bulunmuyor.")



@bot.command()
async def pençe(ctx):
    mesaj = "**Rakibini Boynundan/Vücudundan pençeledin. İstersen ağır yaralayabilir istersen normal yaralayabilirsin.**"
    
    embed = discord.Embed(description=mesaj, color=discord.Color.purple())  # Pençe komutunun rengi mor
    embed.set_image(url="https://daizdje8zyv90.cloudfront.net/wp-content/uploads/2016/10/The-Wolfman-2010.gif")
    embed.set_footer(text="❁ ┃ Harry Potter Roleplay")
    
    await ctx.send(embed=embed)

@bot.command()
async def ısır(ctx):
    mesaj = "**Rakibini Boynundan/Kolundan ısırdın. İstersen ağır yaralayabilir istersen normal yaralayabilirsin.**"
    
    embed = discord.Embed(description=mesaj, color=discord.Color.red())  # Isır komutunun rengi kırmızı
    embed.set_image(url="https://media.tenor.com/zfJ345PtJs4AAAAC/vampire-fangs-vampire-bite.gif")
    embed.set_footer(text="❁ ┃ Harry Potter Roleplay")
    
    await ctx.send(embed=embed)

client = discord.Client(intents=intents)

# Embed renklerini belirleyin
colors = [0x00ff00, 0x0000ff, 0xff0000, 0xffff00]

# Ev açıklamalarını ve GIF URL'lerini belirleyin
houses = {
    "Slytherin": "**Düşersin belki de Slytherin'e sen,\nBir başkadır sanki oraya giden,\nAmaçları için neler yapmazlar\nAçıklasam bitmez sabaha kadar.**",
    "Ravenclaw": "**Ravenclaw kısmetin belki,\nOradakilerin hiç çıkmaz sesi,\nMantıktır onlarca önemli olan,\nÖyle kurtulurlar tüm sorunladan.**",
    "Hufflepuff": "**Belki de düşersin Hufflepuff'a\nHaksızlığı hemen kaldırıp rafa\nAdalet uğruna savaş verirsin\nHer yere mutluluk götürmek için.**",
    "Gryffindor": "**Seni Gryffindor'a yollarım belki\nZamanla olursun aslanın teki,\nYiğittir orada kalan çocuklar,\nHepsinin yüreği, nah, mangal kadar.**"
}

# Hufflepuff için GIF URL'si
hufflepuff_gif_url = "https://media.tenor.com/UAs0m2U91tUAAAAC/hufflepuff.gif"
slytherin_gif_url = "https://media.tenor.com/xUbaOIunGp4AAAAC/slytherin-hp.gif"
ravenclaw_gif_url = "https://media.tenor.com/Sgm7TzrEQzAAAAAC/harry-potter-ravenclaw.gif"
gryffindor_gif_url = "https://media.tenor.com/mbb_vsQMsVoAAAAC/gryffindor-harrypotter.gif"

@bot.command()
async def hane(ctx):
    # Rastgele bir ev seçmek
    house = random.choice(list(houses.keys()))

    embed = discord.Embed(
        title=house,
        description=houses[house],
        color=random.choice(colors)
    )

 #gif kısmı
    if house == "Hufflepuff":
        embed.set_image(url=hufflepuff_gif_url)

    if house == "Slytherin":
        embed.set_image(url=slytherin_gif_url)

    if house == "Ravenclaw":
        embed.set_image(url=ravenclaw_gif_url)

    if house == "Gryffindor":
        embed.set_image(url=gryffindor_gif_url)

    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def bakiyeaç(ctx, hedef_rol: discord.Role):
    guild = ctx.guild
    collection = db["banka"]  # MongoDB koleksiyonunu tanımla

    for member in hedef_rol.members:
        user_id = member.id
        user_data = para_collection.find_one({'user_id': user_id})

        if user_data is None:
            await ctx.send(f"{member.mention} hesap verileri bulunamadı. Önce bir hesap oluşturmalısınız.")
            continue

        banka_bakiye = user_data.get('banka', 0)

        # Banka bakiyesini açık bir rol ile güncelle
        yeni_banka_bakiye = banka_bakiye  # Örnek olarak 100 Galleon ekleyebilirsiniz

        para_collection.update_one({'user_id': user_id}, {'$set': {'banka': yeni_banka_bakiye}})

        embed = discord.Embed(
            title=f"{member.name}'in Bakiyesi",
            color=0x39FF14  # Neon Yeşil Rengi
        )

    await ctx.send("Etiketlenen roldeki üyelerin banka bakiyeleri açıldı.")


@bakiyeaç.error
async def bakiyekayıtsız_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Bu komudu sadece administrator yetkisine sahip kişiler kullanabilir.")


@bot.command()
@commands.has_permissions(administrator=True)
async def herkesepara(ctx, miktar: int):
    if miktar is None:
        await ctx.send("Lütfen bir miktar belirtin.")
        return

    if miktar <= 0:
        await ctx.send("Sıfır veya negatif bir miktarı ekleyemezsiniz.")
        return

    guild = ctx.guild
    members = guild.members

    for member in members:
        user_id = member.id
        user_data = para_collection.find_one({'user_id': user_id})

        if user_data is None:
            await ctx.send(f"{member.mention} hesap verileri bulunamadı. Önce bir hesap oluşturmalısınız.")
            continue

        banka_bakiye = user_data.get('banka', 0)
        yeni_banka_bakiye = banka_bakiye + miktar

        para_collection.update_one({'user_id': user_id}, {'$set': {'banka': yeni_banka_bakiye}})

        embed = discord.Embed(
            title=f"{member.name}'in Bakiyesi",
            color=0x39FF14  # Neon Yeşil Rengi
        )
        embed.add_field(name="Kasasına Eklendi", value=f"{miktar} Galleon", inline=False)
        embed.add_field(name="Yeni Bakiye", value=f"{yeni_banka_bakiye} Galleon", inline=False)
        embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
        embed.set_image(url="https://art.pixilart.com/2ae3e02271ea136.gif")

        await ctx.send(f"{miktar} Galleon, {member.mention} kullanıcısının kasasına eklendi.", embed=embed)

    await ctx.send("Tüm üyelerin banka hesaplarına para eklendi.")

@herkesepara.error
async def herkesepara_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Bu komudu sadece administrator yetkisine sahip kişiler kullanabilir.")


@bot.command()
@commands.has_permissions(administrator=True)
async def parasıfırla(ctx, hedef: discord.Member = None):
    if hedef is None:
        # Hedef belirtilmediyse, komutun kullanıcı tarafından çağrıldığını varsayalım
        hedef = ctx.author

    user_id = hedef.id
    user_data = para_collection.find_one({'user_id': user_id})

    if user_data is None:
        await ctx.send(f"{hedef.mention} hesap verileri bulunamadı. Önce bir hesap oluşturmalısınız.")
        return

    new_data = {'$set': {'banka': 0, 'nakit': 0}}
    para_collection.update_one({'user_id': user_id}, new_data)

    embed = discord.Embed(
        title=f"{hedef.name}'in Bakiyesi Sıfırlandı",
        color=0x39FF14  # Neon Yeşil Rengi
    )
    embed.add_field(name="Yeni Banka Bakiye", value="0 Galleon", inline=False)
    embed.add_field(name="Yeni Nakit Bakiye", value="0 Galleon", inline=False)
    embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
    embed.set_image(url="https://art.pixilart.com/2ae3e02271ea136.gif")

    await ctx.send(f"{hedef.mention} banka ve nakit bakiyeleri sıfırlandı.", embed=embed)

@parasıfırla.error
async def parasıfırla_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Bu komudu sadece administrator yetkisine sahip kişiler kullanabilir.")

@bot.command()
async def hesapaç(ctx):
    # Rol bilgisini al
    author_roles = [role.id for role in ctx.author.roles]
    
    # İstenen role sahip olup olmadığını kontrol et
    if 1120816848875827214 not in author_roles:
        await ctx.send("Bu komutu kullanma izniniz yok!")
        return
    
    # Sunucudaki tüm üyeler için hesap açma işlemi
    for member in ctx.guild.members:
        user_id = member.id
        user_data = para_collection.find_one({'user_id': user_id})
        
        if user_data is None:
            para_collection.insert_one({'user_id': user_id, 'nakit': 0, 'banka': 0})
    
    await ctx.send("Sunucudaki tüm üyeler için banka hesapları başarıyla oluşturuldu.")

@bot.command()
async def paraver(ctx, hedef: discord.Member, miktar: int):
    if miktar is None:
        await ctx.send("Lütfen bir miktar belirtin.")
        return

    if miktar <= 0:
        await ctx.send("Sıfır veya negatif bir miktarı aktaramazsınız.")
        return

    hedef_id = hedef.id
    user_data_gonderen = para_collection.find_one({'user_id': ctx.author.id})
    user_data_alan = para_collection.find_one({'user_id': hedef_id})

    if user_data_gonderen is None or user_data_alan is None:
        await ctx.send("Gönderici veya alıcı hesap verileri bulunamadı. Önce bir hesap oluşturmalısınız.")
        return

    gonderen_banka_bakiye = user_data_gonderen.get('banka', 0)
    alan_banka_bakiye = user_data_alan.get('banka', 0)

    if gonderen_banka_bakiye < miktar:
        await ctx.send("Yetersiz banka bakiyesi.")
        return

    yeni_gonderen_banka_bakiye = gonderen_banka_bakiye - miktar
    yeni_alan_banka_bakiye = alan_banka_bakiye + miktar

    para_collection.update_one({'user_id': ctx.author.id}, {'$set': {'banka': yeni_gonderen_banka_bakiye}})
    para_collection.update_one({'user_id': hedef_id}, {'$set': {'banka': yeni_alan_banka_bakiye}})

    embed = discord.Embed(
        title=f"{ctx.author.name}'in Bakiyesi",
        color=0x39FF14  # Neon Yeşil Rengi
    )
    embed.add_field(name="Gönderilen Miktar", value=f"{miktar} Galleon", inline=False)
    embed.add_field(name="Yeni Gönderen Nakit Bakiye", value=f"{yeni_gonderen_banka_bakiye} Galleon", inline=False)
    embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
    embed.set_image(url="https://art.pixilart.com/2ae3e02271ea136.gif")

    await ctx.send(f"{miktar} Galleon, {hedef.mention} kullanıcısına gönderildi.", embed=embed)

    # Alıcı bakiyesini güncelle
    embed_alan = discord.Embed(
        title=f"{hedef.name}'in Bakiyesi",
        color=0x39FF14  # Neon Yeşil Rengi
    )
    embed_alan.add_field(name="Alınan Miktar", value=f"{miktar} Galleon", inline=False)
    embed_alan.add_field(name="Yeni Nakit Bakiye", value=f"{yeni_alan_banka_bakiye} Galleon", inline=False)
    embed_alan.set_footer(text='✥ ┃ Harry Potter Roleplay')
    embed_alan.set_image(url="https://art.pixilart.com/2ae3e02271ea136.gif")

    await hedef.send(f"{ctx.author.mention}, size {miktar} Galleon gönderdi.", embed=embed_alan)

@bot.command()
async def parayatır(ctx, miktar: int):
    if miktar is None:
        await ctx.send("Lütfen yatırmak istediğiniz miktarı belirtin.")
        return

    if miktar <= 0:
        await ctx.send("Sıfır veya negatif bir miktar yatıramazsınız.")
        return

    user_id = ctx.author.id
    user_data = para_collection.find_one({'user_id': user_id})

    if user_data is None:
        await ctx.send("Hesap verileriniz bulunamadı. Önce bir hesap oluşturmalısınız.")
        return

    banka_bakiye = user_data.get('banka', 0)
    nakit_bakiye = user_data.get('nakit', 0)

    if nakit_bakiye < miktar:
        await ctx.send("Yetersiz nakit bakiye. Yatırmak istediğiniz miktarı nakit bakiyenizden yatıramazsınız.")
        return

    yeni_banka_bakiye = banka_bakiye + miktar
    yeni_nakit_bakiye = nakit_bakiye - miktar

    para_collection.update_one({'user_id': user_id}, {'$set': {'banka': yeni_banka_bakiye, 'nakit': yeni_nakit_bakiye}})

    embed = discord.Embed(
        title=f"{ctx.author.name}'in Bakiyesi",
        color=0x39FF14  # Neon Yeşil Rengi
    )
    embed.add_field(name="Yatırılan Miktar", value=f"{miktar} Galleon", inline=False)
    embed.add_field(name="Yeni Banka Bakiye", value=f"{yeni_banka_bakiye} Galleon", inline=False)
    embed.add_field(name="Yeni Nakit Bakiye", value=f"{yeni_nakit_bakiye} Galleon", inline=False)
    embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
    embed.set_image(url="https://cdn.pixabay.com/animation/2023/06/13/15/13/15-13-37-55_512.gif")

    await ctx.send(f"{miktar} Galleon nakit bakiyenizden banka hesabınıza yatırıldı.", embed=embed)


@bot.command()
async def paraçek(ctx, miktar: int):
    if miktar is None:
        await ctx.send("Lütfen çekmek istediğiniz miktarı belirtin.")
        return

    if miktar <= 0:
        await ctx.send("Sıfır veya negatif bir miktar çekemezsiniz.")
        return

    user_id = ctx.author.id
    user_data = para_collection.find_one({'user_id': user_id})

    if user_data is None:
        await ctx.send("Hesap verileriniz bulunamadı. Önce bir hesap oluşturmalısınız.")
        return

    banka_bakiye = user_data.get('banka', 0)
    nakit_bakiye = user_data.get('nakit', 0)

    if banka_bakiye < miktar:
        await ctx.send("Yetersiz banka bakiyesi. Çekmek istediğiniz miktarı banka bakiyenizden çekemezsiniz.")
        return

    yeni_banka_bakiye = banka_bakiye - miktar
    yeni_nakit_bakiye = nakit_bakiye + miktar

    para_collection.update_one({'user_id': user_id}, {'$set': {'banka': yeni_banka_bakiye, 'nakit': yeni_nakit_bakiye}})

    embed = discord.Embed(
        title=f"{ctx.author.name}'in Bakiyesi",
        color=0x39FF14  # Neon Yeşil Rengi
    )
    embed.add_field(name="Çekilen Miktar", value=f"{miktar} Galleon", inline=False)
    embed.add_field(name="Yeni Banka Bakiye", value=f"{yeni_banka_bakiye} Galleon", inline=False)
    embed.add_field(name="Yeni Nakit Bakiye", value=f"{yeni_nakit_bakiye} Galleon", inline=False)
    embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
    embed.set_image(url="https://cdn.pixabay.com/animation/2023/06/13/15/12/15-12-37-87_512.gif")

    await ctx.send(f"{miktar} Galleon banka hesabınızdan çekildi.", embed=embed)

@bot.command()
async def bakiye(ctx, member: discord.Member = None):
    user_id = ctx.author.id if member is None else member.id
    user_data = para_collection.find_one({'user_id': user_id})

    if user_data is None:
        await ctx.send("Bakiye verileri bulunamadı. Yeni bir hesap oluşturuluyor...")
        para_collection.insert_one({'user_id': user_id, 'nakit': 0, 'banka': 0})
        user_data = para_collection.find_one({'user_id': user_id})

    nakit_bakiye = user_data.get('nakit', 0)
    banka_bakiye = user_data.get('banka', 0)

    embed = discord.Embed(
        title=f"{ctx.author.name if member is None else member.name}'in Bakiyesi",
        color=discord.Color.red()
    )
    embed.add_field(name=":moneybag: Nakit Bakiye", value=f"{nakit_bakiye} Galleon", inline=False)
    embed.add_field(name=":coin: Banka Bakiye", value=f"{banka_bakiye} Galleon", inline=False)
    embed.set_image(url="https://media.giphy.com/media/1lwTRgQYWYaOxovDQH/giphy.gif")
    embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def paraekle(ctx, hedef: discord.Member, miktar: int):
    if miktar is None:
        await ctx.send("Lütfen bir değer girin.")
        return

    if miktar <= 0:
        await ctx.send("Sıfır veya negatif bir değeri ekleyemezsiniz.")
        return

    hedef_id = hedef.id
    user_data = para_collection.find_one({'user_id': hedef_id})

    if user_data is None:
        await ctx.send("Hedef kullanıcının hesabı bulunamadı.")
        return

    bakiye = user_data.get('banka', 0)
    yeni_bakiye = bakiye + miktar

    para_collection.update_one({'user_id': hedef_id}, {'$set': {'banka': yeni_bakiye}})

    embed = discord.Embed(
        title=f"{hedef.name}'in Bakiyesi",
        color=0x39FF14  # Neon Yeşil Rengi
    )
    embed.add_field(name="Kasasına Eklendi", value=f"{miktar} Galleon", inline=False)
    embed.add_field(name="Yeni Bakiye", value=f"{yeni_bakiye} Galleon", inline=False)
    embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
    embed.set_image(url="https://art.pixilart.com/2ae3e02271ea136.gif")

    await ctx.send(f"{hedef.mention} kullanıcısının kasasına {miktar} Galleon eklendi.", embed=embed)

    # Bakiye güncellemesi
    user_data = para_collection.find_one({'user_id': ctx.author.id})
    nakit_bakiye = user_data.get('nakit', 0)  # Nakit bakiye
    banka_bakiye = user_data.get('banka', 0)  # Banka bakiye

    embed = discord.Embed(
        title=f"{ctx.author.name}'in Bakiyesi",
        color=discord.Color.red()
    )
    embed.add_field(name=":moneybag: Nakit Bakiye", value=f"{nakit_bakiye} Galleon", inline=False)
    embed.add_field(name=":coin: Banka Bakiye", value=f"{banka_bakiye} Galleon", inline=False)
    embed.set_image(url="https://media.giphy.com/media/1lwTRgQYWYaOxovDQH/giphy.gif")
    embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
 
    await ctx.send(embed=embed)

@paraekle.error
async def paraekle_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Bu komudu sadece administrator yetkisine sahip kişiler kullanabilir.")



hortkuluk_haklari = 7

# Hortkuluk komutu
@bot.command()
async def hortkuluk(ctx):
    global hortkuluk_haklari

    # Sadece belirli bir role sahip kullanıcılar için kontrol
    allowed_role_id = 1120816848758386839  # "1120816848758386839" ID'li rol
    user = ctx.message.author
    user_roles = [role.id for role in user.roles]
    
    if allowed_role_id in user_roles:
        if hortkuluk_haklari > 0:
            hortkuluk_haklari -= 1
            embed = discord.Embed(description="Ruhundan bir parça daha en yakınındaki cansız eşyaya geçti!", color=0xFFA500)
            await ctx.send(embed=embed)
            embed = discord.Embed(description=f"Kalan hortkuluk hakkınız: {hortkuluk_haklari}", color=0xFFA500)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description="Maalesef ruhundan verebileceğin başka parça kalmadı!", color=0xFFA500)
            await ctx.send(embed=embed)
    else:
        await ctx.send("Bu komutu kullanma izniniz yok!")

# Hortkuluk sıfırlama komutu
@bot.command()
async def hortkuluksıfırla(ctx):
    global hortkuluk_haklari

    # Sadece belirli bir role sahip kullanıcılar için kontrol
    allowed_role_id = 1120816848758386839  # "1120816848758386839" ID'li rol
    user = ctx.message.author
    user_roles = [role.id for role in user.roles]
    
    if allowed_role_id in user_roles:
        hortkuluk_haklari = 7
        embed = discord.Embed(description="Hortkuluk hakkınız yenilendi!", color=0xFFA500)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Bu komutu kullanma izniniz yok!")

@bot.command()
async def zihinbend(ctx):
    # Kullanıcının belirli bir role sahip olup olmadığını kontrol et
    role_id = 1120816848770957370  # Rol ID'si buraya eklenir
    role = discord.utils.get(ctx.author.roles, id=role_id)

    if role is not None:
        # Olumsuz metni belirli bir olasılıkla ekleyin
        if random.random() < 0.5:
            message = f"***{ctx.author.mention}, zihnini koruyamadın!***"
        else:
            message = f"***{ctx.author.mention}, zihnini koruyorsun!***"

        embed = discord.Embed(description=message)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Bu komutu kullanma izniniz yok! Sadece **zihinbend** rolüne sahip kişiler kullanabilir.")

@bot.command()
async def zihinefend(ctx, user: discord.User = None):
    # Kullanıcının belirli bir role sahip olup olmadığını kontrol et
    role_id = 1120816848770957371  # Rol ID'si buraya eklenir
    role = discord.utils.get(ctx.author.roles, id=role_id)

    if user is None:
        await ctx.send(f"{ctx.author.mention} Lütfen zihninin okunmasını istediğiniz kişiyi seçiniz!")
    elif role is not None:
        # Olumsuz metni belirli bir olasılıkla ekleyin
        if random.random() < 0.5:
            message = f"***{ctx.author.mention}, {user.mention}'nin zihnini okuyamadı!***"
        else:
            message = f"***{ctx.author.mention}, {user.mention}'nin zihnini okuyor!***"

        embed = discord.Embed(description=message)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Bu komutu kullanma izniniz yok! Sadece **zihinefend** rolüne sahip kişiler kullanabilir.")


@bot.command()
async def kılıç(ctx):
    # Kullanıcının belirli bir role sahip olup olmadığını kontrol et
    role_id = 1120816848758386837  # Rol ID'si buraya eklenir
    role = discord.utils.get(ctx.author.roles, id=role_id)

    if role is not None:
        # Olumsuz metni belirli bir olasılıkla ekleyin
        if random.random() < 0.5:
            message = f"{ctx.author.mention} **Kılıcını salladın, ancak rakibini YARALAYAMADIN!**"
        else:
            message = f"{ctx.author.mention} **Kılıcını salladın ve rakibini YARALADIN!**"

        gif_url = "https://media.tenor.com/Tfg3X1RRMjsAAAAC/getting-sword-alex-boye.gif"
        embed = discord.Embed(description=message)
        embed.set_image(url=gif_url)
        embed.set_footer(text='❁ ┃Harry Potter Roleplay')
        await ctx.send(embed=embed)
    else:
        await ctx.send("Bu komutu kullanma izniniz yok!")

@bot.command()
async def gryffindorunkılıcı(ctx):
    # Kullanıcının belirli bir role sahip olup olmadığını kontrol et
    role_id = 1120816848770957363  # Rol ID'si buraya eklenir
    role = discord.utils.get(ctx.author.roles, id=role_id)

    if role is not None:
        # Olumsuz metni belirli bir olasılıkla ekleyin
        if random.random() < 0.5:
            message = f"{ctx.author.mention} **Gryffindor'un kılıcını salladın, ancak rakibine 'hafif yaralamak, ağır yaralamak, öldürmek' bu hamlelerden birini YAPAMADIN!**"
        else:
            message = f"{ctx.author.mention} **Gryffindor'un kılıcını salladın ve rakibine 'hafif yaralamak, ağır yaralamak, öldürmek' bu hamlelerden birini YAPTIN!**"

        gif_url = "https://media.tenor.com/Mt8NLnaQnvEAAAAC/harry-potter-sword.gif"
        embed = discord.Embed(description=message)
        embed.set_image(url=gif_url)
        embed.set_footer(text='❁ ┃ Harry Potter Roleplay')
        await ctx.send(embed=embed)
    else:
        await ctx.send("Bu komutu kullanma izniniz yok!")

@bot.command()
async def normalhançer(ctx):
    # Kullanıcının belirli bir role sahip olup olmadığını kontrol et
    role_id = 1120816848758386838  # Rol ID'si buraya eklenir
    role = discord.utils.get(ctx.author.roles, id=role_id)

    if role is not None:
        # Olumsuz metni belirli bir olasılıkla ekleyin
        if random.random() < 0.5:
            message = f"{ctx.author.mention} **Normal hançerini salladın, ancak rakibine 'yaralama' bu hamleyi YAPAMADIN!**"
        else:
            message = f"{ctx.author.mention} **Normal hançerini salladın ve rakibine 'yaralama' bu hamleyi YAPTIN!**"

        gif_url = "https://media.tenor.com/jwkh-RgpS-sAAAAC/argent-allison.gif"
        embed = discord.Embed(description=message)
        embed.set_image(url=gif_url)
        embed.set_footer(text='❁ ┃ Harry Potter Roleplay')
        await ctx.send(embed=embed)
    else:
        await ctx.send("Bu komutu kullanma izniniz yok!")

@bot.command()
async def rovenanınhançeri(ctx):
    # Kullanıcının belirli bir role sahip olup olmadığını kontrol et
    role_id = 1120816848770957365  # Rol ID'si buraya eklenir
    role = discord.utils.get(ctx.author.roles, id=role_id)

    if role is not None:
        # Olumsuz metni belirli bir olasılıkla ekleyin
        if random.random() < 0.5:
            message = f"{ctx.author.mention} **Rovena'nın hançerini salladın, ancak rakibine 'etki altına alma, ağır yaralama, öldürme' bu hamlelerden birini YAPAMADIN!**"
        else:
            message = f"{ctx.author.mention} **Rovena'nın hançerini salladın ve rakibine 'etki altına alma, ağır yaralama, öldürme' bu hamlelerden birini YAPTIN!**"

        gif_url = "https://s6.gifyu.com/images/S89lC.gif"
        embed = discord.Embed(description=message)
        embed.set_image(url=gif_url)
        embed.set_footer(text='❁ ┃ Harry Potter Roleplay')
        await ctx.send(embed=embed)
    else:
        await ctx.send("Bu komutu kullanma izniniz yok!")

@bot.command()
async def düello(ctx):
    zarlar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    random_result = random.choice(zarlar)
    asagucu = 0

    if any(role.id in [1120816848779366558, 1120816848779366557] for role in ctx.author.roles):
        asagucu = 11  # efsanevi
    elif any(role.id in [1120816848779366556, 1120816848779366555] for role in ctx.author.roles):
        asagucu = 10  # epik
    elif any(role.id in [1139500117414658148, 1120816848779366554] for role in ctx.author.roles):
        asagucu = 7  # elit
    elif any(role.id in [1120816848779366553, 1120816848779366552] for role in ctx.author.roles):
        asagucu = 5  # nadir

    if asagucu == 0:
        await ctx.reply('Düello yapmak için ilk önce kendine bir asa satın almalısın.')
        return

    guc = random_result + asagucu

    embed = discord.Embed(
        title='Düello Sonucu',
        color=0xFF0000
    )

    embed.add_field(name='🎲 Zar', value=f'{random_result}', inline=False)
    embed.add_field(name='<:a:720097422499643443> Asa Gücü', value=f'{asagucu}', inline=False)
    embed.add_field(name='<:a:715354783405441087> Toplam', value=f'{guc}', inline=False)
    embed.add_field(name='Düello Komudunu Kullanan Kişi:', value=ctx.author.mention)

    embed.set_image(url='https://media.tenor.com/k8A6_miFkgoAAAAd/ratio-harry-potter-lol-ashdon.gif')
    embed.set_footer(text='❁ ┃ Harry Potter Roleplay')

    await ctx.send(embed=embed)


@bot.command()
async def büyü(ctx, büyü_adı):
    rich = ctx.author
    tag = ctx.author
    büyü_adı = büyü_adı.lower()  # Büyü adını küçük harf yapalım.

    if büyü_adı == "wingardiumleviosa":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **wingardiumleviosa** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/NVvKuKKbJh4AAAAd/ron-weasley-harry-potter.gif")
            embed.set_footer(text='❁ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='❁ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)
    
    if büyü_adı == "lumos":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **lumos** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/d1L2dPzsobYAAAAC/harrypotter-wands.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)

    if büyü_adı == "aguamenti":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **aguamenti** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/OE4Db-INu40AAAAC/dumbledore-albus.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "nox":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **nox** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://cdn-longterm.mee6.xyz/plugins/commands/images/979410357388976138/53f5fe86db80766a5d2243029de160cb6348f2965bb96a9bd8c44f8916ce2dfa.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "accio":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **accio** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/KIpV4rHwju0AAAAC/harry-potter-wand.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "incendio":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **incendio** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/un4UXCaukiQAAAAC/stranger-things-fire.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "evertestatum":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **evertestatum** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/XPnGS8TFJQQAAAAC/harry-potter-spells-harry-potter.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "expelliarmus":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **expelliarmus** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/zBzAptUTt_wAAAAd/expelliarmus.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "sluglus":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **sluglus** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/XqsbA9D2KggAAAAd/sick-harry-potter.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "protego":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **protego** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/1qnjgoauwFAAAAAC/protego-maxima.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "hover":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **hover** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/ShL22n9trgMAAAAC/cat-hover.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "depulso":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **depulso** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/7FXy5MJZqE4AAAAC/hermione-granger-harry-potter.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "rictusempra":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **rictusempra** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/s-5ZYMzoMskAAAAd/ricktusempra.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "langlock":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **langlock** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/GMnP23KnEnYAAAAC/patronus-harry-potter.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "bombarda":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **bombarda** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/L8W2NWt5TvMAAAAC/hermione-bombarda-harry-potter.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "stupefy":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **stupefy** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/HgJ8tf3h7YMAAAAC/hermione-granger.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "locomotor":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **locomotor** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/obfyvR_k4aIAAAAC/molly-weasley.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "incarcerous":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **incarcerous** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/kOcL9e_28_cAAAAC/harry-potter-hp.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "conjunctivitis":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **conjunctivitis** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/lfSC9l7R6WgAAAAC/ron-weasley-harry-potter.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "flagrante":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **flagrante** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/yzUJiOzIQKsAAAAC/onco-harry-potter.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "ascendio":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **ascendio** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/KsDtNl0HM_8AAAAC/harry-potter.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "engorgio":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **engorgio** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/9H8t6ZSYs-oAAAAC/tght.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "episkey":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **episkey** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/lO3jkVGveiUAAAAC/hermione-granger.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "aquaerecto":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **aquaerecto** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/8xE-36hnC68AAAAC/harry-potter-water.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "brackiumemmendo":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **brackiumemmendo** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/eK12mSIqg14AAAAd/harry-potter-brackium-emendo.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "colloportus":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **colloportus** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/UUt5Uen-cO8AAAAd/harry-potter-harry-potter-vs-voldemort.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "arestomomentum":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **arestomomentum** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/LsAx9ipmqIEAAAAC/areto-momentum-albus-dumbeldore.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "carpepotrus":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **carpepotrus** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/CsRjUpdCKKcAAAAC/tamponpotter-harrypotter.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "carperetractum":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **carperetractum** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/HBf2airWb0YAAAAC/dumbledore-harry-potter.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "distimi":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **distimi** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/md4Fv1rdl5wAAAAC/harry-potter-phoenix.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "duro":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **duro** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/e31i4jCpe9IAAAAC/dumbledore-albus-percival-wulfric-brian-dumbledore.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "ımpedimenta":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **ımpedimenta** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/FjXcf-PfJnkAAAAC/harry-potter.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "oblivate":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **oblivate** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/c9rYFLsrGmwAAAAC/potter.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "fidelius":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **fidelius** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/sS6786EikdwAAAAC/harry-potter.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "protegodiabolica":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **protegodiabolica** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/tuCp6SF77qkAAAAC/johnny-depp-gellert-grindelwald.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "deletrius":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **deletrius** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/n4va7lXhMKEAAAAd/harry-potter-quirrell.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "salviohexia":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **salviohexia** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/paJwYeoHAsgAAAAd/hermione-granger.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "sectumsempra":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **sectumsempra** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/SMIq3i_b6HcAAAAC/sectumsempra-harry-potter.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "vulnerasanentur":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **vulnerasanentur** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/k8A6_miFkgoAAAAd/ratio-harry-potter-lol-ashdon.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "confringo":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **confringo** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/RlEuaBX7PLwAAAAC/harry-potter.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "silencio":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **silencio** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/trpo0eH8TeIAAAAC/dumbledore-albus-percival-wulfric-brian-dumbledore.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "fiantoduri":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **fiantoduri** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/p4VdDhUPY4AAAAAC/harry-potter-slughorn.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "descendio":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **descendio** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/Rfk3KapYYLcAAAAC/fireball-hell-hole.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "ferula":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **ferula** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://heyitszel.files.wordpress.com/2017/06/midorima_taped-fingers.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "avadakedavra":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **avadakedavra** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/yhFq6N5tvUEAAAAC/avada-kadavra-star-wars.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "cruciatus":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **cruciatus** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/eNTkZ7JlxyQAAAAC/voldemort-power.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "imperio":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **imperio** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/0XFw38q1byMAAAAC/imperio-harry-potter.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "sonorus":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **sonorus** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/R9GndAWEirUAAAAC/harry-potter-pointing.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "expectopatronum":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **expectopatronum** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/HRQdjO4_U4AAAAAC/harry-potter.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    if büyü_adı == "morsmordre":
        # %50 ihtimalle olumlu ya da olumsuz sonuç alalım
        olumlu = random.choice([True, False])

        if olumlu:
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **morsmordre** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/Z8MIDuFbVXgAAAAd/esteestugifame-harry-potter.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            
            await ctx.send(embed=embed)

    elif büyü_adı == "legilimens":
        karanlik_lord_role_id = 1120816848863252590
        olumlu = random.choice([True, False])  # %50 ihtimalle olumlu veya olumsuz sonuç

        if olumlu and discord.utils.get(ctx.author.roles, id=karanlik_lord_role_id):
            embed = discord.Embed(
                title=f'{ctx.author} asasını kaldırdı ve...',
                description=f'Başarıyla <@!{rich.id}> kişisi **Legilimens** büyüsünü yaptı :magic_wand: ',
                color=discord.Color(0x800080)
            )
            embed.set_image(url="https://media.tenor.com/k7Pys9PpjnAAAAAC/magic-fantasy.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            await ctx.send(embed=embed)
        elif not discord.utils.get(ctx.author.roles, id=karanlik_lord_role_id):
            await ctx.send("Bu büyüyü kullanmanız için **Karanlık Lord** olmanız gerek!")
        else:
            embed = discord.Embed(
                title=f'Bir şeyler ters gitti!',
                description=f'<@!{rich.id}> asasını kaldırdı ancak büyü biraz ters gitti... :x:',
                color=discord.Color(0xFF0000)  # Kırmızı renk
            )
            embed.set_image(url="https://media.tenor.com/sG0daOlIDZwAAAAC/harry-potter-hold.gif")
            embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
            await ctx.send(embed=embed)


@bot.command()
async def fzar(ctx):
    zarlar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    random_result = random.choice(zarlar)
    fiziksel_guc = 0

    if any(role.id in [1120816848745812051, 1120816848770957368] for role in ctx.author.roles):
        fiziksel_guc = 10  # İlk rol için fiziksel güç
    elif any(role.id in [1120816848745812050, 1120816848770957366] for role in ctx.author.roles):
        fiziksel_guc = 7  # İkinci rol için fiziksel güç

    if fiziksel_guc == 0:
        await ctx.send("Bu komudu kullanabilmeniz için '**Alfa kurt, Beta kurt, Safkan İnsanüstü Güç veya İnsanüstü güç**' rollerinden en az birine sahip olmanız gerekir.")
        return

    guc = random_result + fiziksel_guc

    embed = discord.Embed(
        title=f"{ctx.author.name} fiziksel zarını attı",
        description=f"Zarlar atıldı ve sonuç {random_result}\nFiziksel Gücünüz: {fiziksel_guc}",
        color=discord.Color(0x800080)
    )
    embed.add_field(name='🎲 Zar', value=f'{random_result}', inline=False)
    embed.add_field(name=':zap: Fiziksel Güç', value=f'{fiziksel_guc}', inline=False)
    embed.add_field(name='<:a:715354783405441087> Toplam', value=f'{guc}', inline=False)
    embed.set_image(url="https://images-ext-1.discordapp.net/external/IorlEVqzTl90pQcwfABrijqksk2_ZY_JTzSt2REmK6I/https/64.media.tumblr.com/e5a9497a6adab05b5b00d34ff72ecc39/1f5f5c6c85b38ef9-19/s400x600/877ce61c708ee4e710f9bd85d79157565238bc35.gif")
    embed.set_footer(text='✥ ┃ Harry Potter Roleplay')

    await ctx.send(embed=embed)



@bot.command()
async def büyüler(ctx):
    büyüler_dict = {
        "1.SINIF BÜYÜLER": ["wingardiumleviosa", "aguamenti", "lumos", "nox", "accio", "incendio"],
        "2.SINIF BÜYÜLER": ["evertestatum", "expelliarmus", "sluglus", "protego"],
        "3.SINIF BÜYÜLER": ["hover", "depulso", "rictusempra", "langlock"],
        "4.SINIF BÜYÜLER": ["bombarda", "stupefy", "locomotor", "incarcerous", "conjunctivitis", "flagrante", "ascendio", "engorgio", "episkey"],
        "5.SINIF BÜYÜLER": ["aquaerecto", "brackiumemmendo", "colloportus", "arestomomentum", "carpepotrus", "carperetractum"],
        "6.SINIF BÜYÜLER": ["distimi", "duro", "ımpedimenta", "oblivate", "fidelius"],
        "7.SINIF BÜYÜLER": ["deletrius", "salviohexia", "sectumsempra", "vulnerasanentur", "confringo"],
        "MEZUN VATANDAŞ BÜYÜLERİ": ["silencio", "fiantoduri", "descendio", "ferula", "avadakedavra", "cruciatus", "imperio", "sonorus", "expectopatronum", "legilimens"],
        "KARANLIK TARAF VE KARANLIK LORD BÜYÜLERİ": ["morsmordre (Karanlık Lord/Karanlık Tarafa Özel)", "legilimens (Karanlık Lord'a Özel)"]
    }

    büyüler_mesaj = ""
    for sınıf, büyüler in büyüler_dict.items():
        büyüler_mesaj += f"**{sınıf}**\n"
        for büyü in büyüler:
            büyüler_mesaj += f"{büyü}\n"
        büyüler_mesaj += "--------------------------------------------------\n"

    embed = discord.Embed(
        title="Büyüler Listesi",
        description=büyüler_mesaj,
        color=0x000000
    )
    embed.set_footer(text="✥ ┃ Harry Potter Roleplay")

    await ctx.send(embed=embed)

@bot.command()
async def zar(ctx):
    zarlar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    random_sonuc = random.choice(zarlar)

    embed = discord.Embed(
        title=f"{ctx.author.name} zarını attı",
        description=f"Zarlar atıldı ve sonuç {random_sonuc}",
        color=0x97ffff
    )
    embed.set_image(url="https://images-ext-1.discordapp.net/external/IorlEVqzTl90pQcwfABrijqksk2_ZY_JTzSt2REmK6I/https/64.media.tumblr.com/e5a9497a6adab05b5b00d34ff72ecc39/1f5f5c6c85b38ef9-19/s400x600/877ce61c708ee4e710f9bd85d79157565238bc35.gif")
    embed.set_footer(text='✥ ┃ The Harry Potter RP')

    await ctx.send(embed=embed)

@bot.command()
async def kurt(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author

    ihtimal = [1, 2]
    random_sonuc = random.choice(ihtimal)

    if random_sonuc == 1:
        embed = discord.Embed(
            title=f"{member.display_name} Kurt adama dönüşmeye çalıştın ve başardın. Artık kurt formundasın. Sadece kendi ırkın ile zihinden konuşabilirsin! :wolf: Auuuuuuuu",
            description="",

            color=0x000000
        )
        embed.set_footer(text='✥ ┃ Harry Potter Roleplay')
        embed.set_image(url="https://img-s3.onedio.com/id-5d84d0c03a54444666a5f692/rev-0/w-600/h-250/f-gif/s-cd3090c2272cd48a10ee7582987dfaaf878d78b1.gif")
        await ctx.send(embed=embed)
    else:
        embed2 = discord.Embed(
            title=f"{member.display_name} Kurda Dönüşmeyi Başaramadı!",
            description="",
            color=0x000000
        )
        embed2.set_footer(text='✥ ┃ Harry Potter Roleplay')
        embed2.set_image(url="https://img-s3.onedio.com/id-5d84d0c03a54444666a5f692/rev-0/w-600/h-250/f-gif/s-cd3090c2272cd48a10ee7582987dfaaf878d78b1.gif")
        await ctx.send(embed=embed2)

# Kanal ID'si
kanal_id = 1125051625153757224  # Kanalın gerçek ID'si ile değiştirin

@bot.command()
async def at(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    kanal = bot.get_channel(kanal_id)
    await ctx.send(f"{member.mention} adlı üye sunucudan '{reason}' atıldı!")
    await kanal.send(f"{member.mention} adlı üye sunucudan '{reason}' atıldı! <@&1120816848875827212>")

@bot.command()
async def banla(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    kanal = bot.get_channel(kanal_id)
    await ctx.send(f"{member.mention} adlı üye '{reason}' sebebiyle sunucudan yasaklandı!")
    await kanal.send(f"{member.mention} adlı üye '{reason}' sebebiyle sunucudan yasaklandı! <@&1120816848875827212>")

@bot.command()
async def unban(ctx, member: discord.User):
    banned_users = await ctx.guild.bans()
    for entry in banned_users:
        if entry.user == member:
            await ctx.guild.unban(member)
            kanal = bot.get_channel(kanal_id)
            await ctx.send(f"{member.mention} adlı üyenin yasaklaması kaldırıldı!")
            await kanal.send(f"{member.mention} adlı üyenin yasaklaması kaldırıldı! <@&1120816848875827212>")
            return

@bot.command()
async def sesikapa(ctx, member: discord.Member, *, reason=None):
    role = discord.utils.get(ctx.guild.roles, name="Susturulmuş")  # 'Susturulmuş' rolünü oluşturun
    if not role:
        role = await ctx.guild.create_role(name="Susturulmuş")
        for channel in ctx.guild.text_channels:
            await channel.set_permissions(role, send_messages=False)
    await member.add_roles(role, reason=reason)
    kanal = bot.get_channel(kanal_id)
    await ctx.send(f"{member.mention} adlı üye '{reason}' sebebiyle susturuldu!")
    await kanal.send(f"{member.mention} adlı üye '{reason}' sebebiyle susturuldu! Dikkat: <@761555500164186116>")

@bot.command()
async def sesiaç(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Susturulmuş")
    if role in member.roles:
        await member.remove_roles(role)
        kanal = bot.get_channel(kanal_id)
        await ctx.send(f"{member.mention} adlı üyenin susturması kaldırıldı!")
        await kanal.send(f"{member.mention} adlı üyenin susturması kaldırıldı! <@761555500164186116>")

# "Botdurum" komutu
@bot.command()
async def botdurum(ctx):
    # Şu anki zamanı alın
    su_anki_zaman = datetime.datetime.now()

    # Embed mesajını oluşturun
    embed = discord.Embed(title="Bot Durum:\n\nBot Aktif, Tüm Sistemler Çalışıyor Ve Devrede, Herhangi Bir Aksaklık Olursa KASADİOVALE#0001 Ulaşınız. İyi Günler! :man_mage::skin-tone-2: \n\n:white_check_mark: :white_check_mark: :white_check_mark: :white_check_mark: :white_check_mark:  ", color=0x800080)  # Mor renginde bir embed
    embed.add_field(name=":alarm_clock: Aktiflik Saati", value=su_anki_zaman.strftime("%H:%M:%S"), inline=False)
    embed.add_field(name=":date: Tarih", value=su_anki_zaman.strftime("%d/%m/%Y"), inline=False)
    embed.add_field(name=":star2: Gün", value=su_anki_zaman.strftime("%A"), inline=False)

    # Embed mesajını gönderin
    await ctx.send(embed=embed)

@bot.command()
async def botadurum(ctx):
    su_anki_zaman = datetime.datetime.now()

    # İzin verilen rol ID'si
    izin_verilen_rol_id = 1245799328438812672  # Bu ID'yi belirli bir rolün ID'siyle değiştirin

    # Kullanıcı kontrolü
    if any(role.id == izin_verilen_rol_id for role in ctx.message.author.roles):
        embed = discord.Embed(title="Bot Durum:\n\nBot Aktif, Tüm Sistemler Devrede! İyi Günler! :man_mage::skin-tone-2: \n\n:white_check_mark: :white_check_mark: :white_check_mark: :white_check_mark: :white_check_mark: ", color=0x00FF00)
        embed.add_field(name=":alarm_clock: Aktiflik Saati", value=su_anki_zaman.strftime("%H:%M:%S"), inline=False)
        embed.add_field(name=":date: Tarih", value=su_anki_zaman.strftime("%d/%m/%Y"), inline=False)
        embed.add_field(name=":star2: Gün", value=su_anki_zaman.strftime("%A"), inline=False)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Bu komutu kullanma izniniz yok. Bu komutu sadece 'Owner' rolüne sahip kullanıcılar kullanabilir.")


@bot.command()
async def botidurum(ctx):
    su_anki_zaman = datetime.datetime.now()
    izin_verilen_rol_id = 1245799328438812672

    if any(role.id == izin_verilen_rol_id for role in ctx.message.author.roles):
        embed = discord.Embed(title="Bot Durum:\n\nBot İnaktif, Tüm Sistemler Devredışı! İyi Günler! :man_mage::skin-tone-2: \n\n:white_check_mark: :white_check_mark: :white_check_mark: :white_check_mark: :white_check_mark: ", color=0xFF0000)
        embed.add_field(name=":alarm_clock: Aktiflik Saati", value=su_anki_zaman.strftime("%H:%M:%S"), inline=False)
        embed.add_field(name=":date: Tarih", value=su_anki_zaman.strftime("%d/%m/%Y"), inline=False)
        embed.add_field(name=":star2: Gün", value=su_anki_zaman.strftime("%A"), inline=False)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Bu komutu kullanma izniniz yok. Bu komutu sadece 'Owner' rolüne sahip kullanıcılar kullanabilir.")


@bot.command()
async def botbdurum(ctx):
    su_anki_zaman = datetime.datetime.now()
    izin_verilen_rol_id = 1245799328438812672

    if any(role.id == izin_verilen_rol_id for role in ctx.message.author.roles):
        embed = discord.Embed(title="Bot Durum:\n\nBot Bakımda, Tüm Sistemler Yarı Aktif. Aksaklıklar Yaşanabilir En Yakın Zamanda Düzeltilecektir. İyi Günler! :man_mage::skin-tone-2: \n\n:white_check_mark: :white_check_mark: :white_check_mark: :white_check_mark: :white_check_mark: ", color=0x0000FF)
        embed.add_field(name=":alarm_clock: Aktiflik Saati", value=su_anki_zaman.strftime("%H:%M:%S"), inline=False)
        embed.add_field(name=":date: Tarih", value=su_anki_zaman.strftime("%d/%m/%Y"), inline=False)
        embed.add_field(name=":star2: Gün", value=su_anki_zaman.strftime("%A"), inline=False)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Bu komutu kullanma izniniz yok. Bu komutu sadece 'Owner' rolüne sahip kullanıcılar kullanabilir.")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if isinstance(message.channel, discord.TextChannel):
        category_id = message.channel.category_id
        if category_id in [1141068839958892694, 1141873373144678400, 1155587917465522186, 1137009792683085937, 1137009844885405776, 1141873326256562196, 1120816861706203146, 1120816860917661744, 1120816860917661737, 1120816859994935386, 1120816859441266690, 1120816858933768202, 1120816858380128354, 1120816858002620447, 1120816858002620441, 1120816857537065092, 1120816857155391499, 1120816856190681097, 1120816856190681091, 1120816855691571335, 1120816854768812055, 1120816854299062444, 1120816852663283825, 1120816851899908184]:
            # Mesajın içeriğini kelimelere ayır ve kelime sayısını hesapla
            words = message.content.split()
            word_count = len(words)
            
            # Kullanıcının daha önce kaydedilmiş bir kaydı var mı kontrol et
            user_record = rp_collection.find_one({"user_id": message.author.id})
            if user_record:
                # Kullanıcının kaydını güncelle
                rp_collection.update_one({"user_id": message.author.id}, {"$inc": {"word_count": word_count}})
            else:
                # Yeni bir kayıt oluştur
                new_record = {"user_id": message.author.id, "user_name": str(message.author), "word_count": word_count}
                rp_collection.insert_one(new_record)


    content = message.content.lower()

    if content == 'sa' or content == 'selam' or content == 'botçuk' or content == 'botcum':
        if content == 'sa' or content == 'selam':
            await message.channel.send(f'Aleyküm selam {message.author.mention} dostum nasılsın?')
            response = await bot.wait_for("message", check=lambda m: m.author == message.author)
            if response.content.lower() == "iyi sen" or "iyiyim sen":
                await message.channel.send(f"Ben her zaman iyiyim :heart_eyes: Sen de hep iyi ol! :sunglasses: :heart: {message.author.mention}")

        if content == 'botçuk' or content == 'botcum':
            await message.channel.send(f'{message.author.mention} Emredin Efendim!')
            response = await bot.wait_for("message", check=lambda m: m.author == message.author)
            if response.content.lower() == "adamsın":
                await message.channel.send(f'Siz de öylesiniz, sağolun efendim! :blush: {message.author.mention}')
            response = await bot.wait_for("message", check=lambda m: m.author == message.author)
            if response.content.lower() == "yat uyu":
                await message.channel.send(f'Tamamdır sahibim, siz nasıl isterseniz! :saluting_face:')

    await bot.process_commands(message)


@bot.command()
async def yardım(ctx):
    embed = discord.Embed(
        title="Yardım Menüsü",
        description="Aşağıdan bir kategori seçin:",
        color=0xE2725B  # Kavuniçi rengi (HEX kodu)
    )
    embed.add_field(
        name="Güvenlik Komutları",
        value="Güvenlik komutları için: `!güvenlik`",
        inline=False
    )
    embed.add_field(
        name="Kayıt Komutları",
        value="Kayıt komutları için: `!kayıt`",
        inline=False
    )
    embed.add_field(
        name="Sistem Komutları",
        value="Sistem komutları için: `!sistem`",
        inline=False
    )
    embed.add_field(
        name="Hogwarts RP Komutları",
        value="Hogwarts RP komutları için: `!hogwarts`",
        inline=False
    )
    embed.add_field(
        name="Para Bilgilendirme Komutları",
        value="Para, Ekonomi İşleyiş Öğrenmek İçin: `!para`",
        inline=False
    )
    embed.set_footer(text='❁ ┃ Harry Potter Roleplay')
    await ctx.send(embed=embed)

@bot.command()
async def güvenlik(ctx):
    embed = discord.Embed(
        title="Güvenlik Komutları",
        description="Aşağıdan bir komut seçin:",
        color=0xFFF400  # Yavruağzı rengi (HEX kodu)
    )
    embed.add_field(
        name="Kick Komudu",
        value="**'!at'** komudu ile herhangi bir üyeyi sunucudan atabilirsiniz. Yalnızca yönetici yetkisine sahip olanlar için geçerlidir.",
        inline=False
    )
    embed.add_field(
        name="Yasaklama Komudu",
        value="**'!banla'** komudu ile herhangi bir üyeyi yasaklayabilirsiniz. Sadece yönetici yetkisine sahip olanlar için geçerlidir.",
        inline=False
    )
    embed.add_field(
        name="Yasak Kaldırma Komudu",
        value="**'!unban'** komudu ile herhangi bir üyenin yasağını kaldırabilirsiniz. Sadece yönetici yetkisine sahip olanlar için geçerlidir.",
        inline=False
    )
    embed.set_footer(text='❁ ┃ Harry Potter Roleplay')
    await ctx.send(embed=embed)

@bot.command()
async def sistem(ctx):
    embed = discord.Embed(
        title="Sistem Komutları",
        description="Aşağıdan bir komut seçin:",
        color=0x39FF14  # Neon yeşil rengi (HEX kodu)
    )
    embed.add_field(
        name="Selamlaşmak İçin",
        value="**Selam** veya **Sa** diyebilirsiniz, bot size cevap verecektir. Ardından nasılsınıza **iyi sen** veya **iyiyim sen** diye cevap verirseniz hoşunuza gidebilecek ve gününüzü güzelleştirebilecek bir cevapla karşı karşıya kalabilirsiniz. :sunglasses:",
        inline=False
    )
    embed.add_field(
        name="Bot İtaat",
        value="**Botcum** veya **Botçuk** diyerek bota itaat ettirebilirsiniz. Botdan cevap geldiğinde **adamsın** derseniz güzel bir cevap alırsınız. :sunglasses:",
        inline=False
    )
    embed.add_field(
        name="Bot Durum Öğrenmek İçin",
        value="**'!botdurum'** komutunu kullanarak botun durumu ve o anki saat, dakika, saniye ve günü öğrenebilirsiniz.",
        inline=False
    )
    embed.add_field(
        name="Bot Aktiflik, İnaktiflik Ve Bakımda Bildirimleri",
        value="**'!botadurum'** bot aktif mesajı, **'!botbdurum'** bot bakımda mesajı, **'!botidurum'** bot inaktif mesajını verir. Şu an sadece bot geliştiricisi bu komutları kullanabilir.",
        inline=False
    )
    embed.add_field(
        name="Mesaj Silme Komudu",
        value="**'!mesajsil [değergir]'** komudu ile dilediğiniz sayıda mesaj silebilirsiniz.",
        inline=False
    )
    embed.add_field(
        name="Kanalda En Son Ne Yazdığını Öğrenme Komudu",
        value="**'!enson'** komudu ile komudu kullandığınız kanaldaki en son yazdığınız mesajı görebilirsiniz.",
        inline=False
    )
    embed.set_footer(text='❁ ┃ Harry Potter Roleplay')
    await ctx.send(embed=embed)

@bot.command()
async def para(ctx):
    embed = discord.Embed(
        title="Para Komutları",
        description="Aşağıdan bir komut seçin:",
        color=0x39FF14  # Neon yeşil rengi (HEX kodu)
    )
    embed.add_field(
        name="Bakiye Öğrenmek Veya Banka Hesabı Açmak",
        value="**'!bakiye'** komudunu kullanarak bakiyenizi veya etiketlediğiniz kişinin bakiyesini öğrebilirsiniz ya da daha önce banka hesabı oluşturmadıysanız oluşturabilirsiniz. Bol kazançlar!",
        inline=False
    )
    embed.add_field(
        name="Para Yatırma",
        value="**'!parayatır'** komudu ile nakitinizde olan parayı dilediğiniz miktarda banka hesabınıza yatırabilirsiniz.",
        inline=False
    )
    embed.add_field(
        name="Para Çekme",
        value="**'!paraçek'** komudunu kullanarak bankanızda bulunan parayı dilediğiniz miktarda nakite çekebilirsiniz.",
        inline=False
    )
    embed.add_field(
        name="Para Transferi",
        value="**'!paraver'** komudunu kullanarak etiketlediğiniz kişiye dilediğiniz miktarda para gönderebilirsiniz. (Yalnızca banka hesabındaki parayı gönderebilirsiniz!)",
        inline=False
    )
    embed.add_field(
        name="Para Ekleme",
        value="**'!paraekle'** komudu ile dilediğiniz sayıda parayı hesabınıza ekleyebilirsiniz. (Yalnızca yöneticiler kullanabilir!)",
        inline=False
    )
    embed.add_field(
        name="Para Sıfırlama",
        value="**'!parasıfırla'** komudu ile tüm paranızı veya etiketleyeceğiniz kişinin tüm parasını sıfırlayabilirsiniz. (Yalnızca yöneticiler kullanabilir!)",
        inline=False
    )
    embed.set_footer(text='❁ ┃ Harry Potter Roleplay')
    await ctx.send(embed=embed)

@bot.command()
async def kayıt(ctx):
    embed = discord.Embed(
        title="Kayıt Komutları",
        description="Aşağıdan bir komut seçin:",
        color=0x8A2BE2  # Mor rengi (HEX kodu)
    )
    embed.add_field(
        name="Kayıt Verilerine Göre Sıralama",
        value="**'/topr'** komudunu kullanarak kayıt verilerine göre bir sıralama çıkarabilirsiniz. Kayıt yetkilisi ve yönetici yetkisine sahip olanlar yapabilir.",
        inline=False
    )
    embed.add_field(
        name="Kayıt Verilerini Gösterme",
        value="**'/rstat'** komudunu kullanarak etiketlediğiniz üyenin veya sizin kayıt verilerinizi gösterir. Kayıt yetkilisi yetkisine sahip olanlar yapabilir.",
        inline=False
    )
    embed.add_field(
        name="Kurallar",
        value="**'/kurallar'** komudunu kullanarak sunucu kurallarını görüntüleyebilirsiniz. Sadece daha önce kuralları kabul etmeyenler ve okumayanlar için geçerlidir.",
        inline=False
    )
    embed.add_field(
        name="Kayıt Edilen Kişi Sayısının Sıfırlanması",
        value="**'/kayıtres'** komudu ile etiketlediğiniz yetkilinin kayıt ettiği kişi sayısını sıfırlar. Kayıt yetkilisi rolüne sahip kişiler açabilir.",
        inline=False
    )
    embed.add_field(
        name="Kayıt Menüsü",
        value="**'/kayıt'** komudu etiketlediğiniz üye için kayıt menüsü açar. Sadece kayıt yetkilisi rolündekiler açabilir.",
        inline=False
    )
    embed.add_field(
        name="İsim Geçmişini Sıfırlama",
        value="**'/isimres'** komudu ile etiketlediğiniz kişinin isim geçmişini sıfırlar. Sadece yönetici yetkisine sahip olanlar yapabilir.",
        inline=False
    )
    embed.add_field(
        name="Data Gösterme",
        value="**'/data'** komudu ile etiketlediğiniz üyenin kayıt datasını, yani geçmişini gösterir. Sadece yönetici yetkisine sahip olanlar yapabilir.",
        inline=False
    )
    embed.add_field(
        name="Blacklist Alma/Çıkarma",
        value="**'/blacklist'** komudu ile etiketlediğiniz üyeyi kara listeye alabilir veya çıkarabilirsiniz. Sadece yönetici yetkisine sahip olanlar yapabilir.",
        inline=False
    )
    embed.add_field(
        name="Kayıt Bilgi Alma",
        value="**'!kayıtbilgi'** komudu ile kaydolmadan önce sorulara cevap verebilirsiniz ve sunucu hakkında bilgi alabilirsiniz!",
        inline=False
    )
    embed.set_footer(text='❁ ┃ Harry Potter Roleplay')
    await ctx.send(embed=embed)

@bot.command()
async def hogwarts(ctx):
    embed = discord.Embed(
        title="Hogwarts RP Komutları",
        description="Aşağıdan bir komut seçin:",
        color=0x0000FF  # Mavi rengi (HEX kodu)
    )
    embed.add_field(
        name="Kurta Dönüşme Komudu",
        value="**'!kurt'** komudu ile kurta dönüşebilirsiniz. Kurta dönüşmeden önce güçlerini kaybetmediğine ve dolunay çıktığına emin ol! :mage_tone2:",
        inline=False
    )
    embed.add_field(
        name="Zar Atma Komudu",
        value="**'!zar'** komudu ile 0 ile 20 arasında bir sayı çekebilirsiniz. Umarım şanslısındır. :man_mage_tone2:",
        inline=False
    )
    embed.add_field(
        name="Büyü Listesi Komudu",
        value="**'!büyüler'** komudu ile büyü listesini açıp Hogwarts'ın özel tariflerini inceleyebilirsiniz! :mage_tone2:",
        inline=False
    )
    embed.add_field(
        name="Fiziksel Zar Komudu",
        value="**'!fzar'** komudu ile fiziksel zar atabilirsiniz. **Alfa Kurt** veya **Safkan İnsan Üstü Güç** komutuna sahip üyeler 10-20 arası zar atar, **Beta Kurt** veya **İnsan Üstü Güç** rolüne sahip üyeler 7-20 arası zar atar. :man_mage_tone2:",
        inline=False
    )
    embed.add_field(
        name="Büyü Kullanımı",
        value="**'!büyü [büyü ismi gir]'** komudunu kullanarak büyü kullanabilirsiniz. Büyülere ulaşmak için büyü listesini açabilirsiniz, komudu **!büyüler**. :man_mage_tone2:",
        inline=False
    )
    embed.add_field(
        name="Düello",
        value="**'!düello'** komudunu kullanarak düello yapabilirsin. İyi olan kazansın. :man_mage_tone2:",
        inline=False
    )
    embed.add_field(
        name="Zihin Okuma",
        value="**'!zihinefend [zihninin okunmasını istediğin kişiyi etiketle]'** komudunu kullanarak zihin okuyabilirsin. Umarım algıların güçlüdür! (Sadece 'zihinefend' rolüne sahipler kullanabilir.) :man_mage_tone2:",
        inline=False
    )
    embed.add_field(
        name="Zihin Koruma",
        value="**'!zihinbend'** komudunu kullanarak zihnini koruyabilirsin. Umarım kendini koruyabilecek güçtesindir! (Sadece 'zihinbend' rolüne sahipler kullanabilir.) :man_mage_tone2:",
        inline=False
    )
    embed.add_field(
        name="Kılıç İle Saldırı",
        value="**'!kılıç'** komudunu kullanarak kılıcını sallayarak saldırıda bulunabilirsin. Kılıcın keskin olsun! (Sadece 'kılıç' rolüne sahipler kullanabilir.) :man_mage_tone2:",
        inline=False
    )
    embed.add_field(
        name="Gryffindor'un Kılıcı İle Saldırı",
        value="**'!gryffindorunkılıcı'** komudunu kullanarak Gryffindor'un kılıcını sallayarak saldırıda bulunabilirsin. Bileğine kuvvet! (Sadece 'Gryffindor'un Kılıcı' rolüne sahipler kullanabilir.) :man_mage_tone2:",
        inline=False
    )
    embed.add_field(
        name="Normal Hançer İle Saldırı",
        value="**'!normalhançer'** komudunu kullanarak Normal Hançer sallayarak saldırı yapabilirsin. Umarım atik ve hızlısındır çünkü buna ihtiyacın olacak! (Sadece 'normal hançer' rolüne sahipler kullanabilir.) :man_mage_tone2:",
        inline=False
    )
    embed.add_field(
        name="Rovena'nın Hançeri İle Saldırı",
        value="**'!rovenanınhançeri'** komudunu kullanarak Rovena'nın Hançerini kullanarak saldırı yapabilirsin. Refleks ve dikkatin umarım iyidir, çok kullanacaksın! (Sadece 'Rovena'nın Hançeri' rolüne sahipler kullanabilir.) :man_mage_tone2:",
        inline=False
    )
    embed.add_field(
        name="Hortkuluk",
        value="**'!hortkuluk'** komudunu kullanarak ruhundan bir parçayı en yakınındaki cansız eşyaya verebilirsin. Sadece 7 hakkın var. Dikkatli kullan! :man_mage_tone2:",
        inline=False
    )
    embed.add_field(
        name="Hortkuluk Hakkı Sıfırlama",
        value="**'!hortkuluksıfırla'** komudunu kullanarak hortkuluk hakkını sıfırlayabilir ve yeniden başlayabilirsin! :man_mage_tone2:",
        inline=False
    )
    embed.add_field(
        name="Hane",
        value="**'!hane'** komudunu kullandığında Slyhterin, Gryffindor, Ravenclaw veya Hufflepuff hanelerinden birini çıkartabilirsin! :man_mage_tone2:",
        inline=False
    )
    embed.add_field(
        name="Isır",
        value="**'!ısır'** komudunu kullanarak ısırıp herhangi birine zarar verebilirsin! :man_mage_tone2:",
        inline=False
    )
    embed.add_field(
        name="Pençe",
        value="**'!pençe'** komudunu kullanarak herhangi birine pençe atabilir ve yaralayabilirsin! :man_mage_tone2:",
        inline=False
    )
    embed.add_field(
        name="RolePlay Kelime Sayısı Listesi Öğrenmek",
        value="**'!rplist'** komudunu kullanarak toplam RP kanallarında yazdığın kelime sayısını gösteren bir listeye ulaşabilirsin! :man_mage_tone2:",
        inline=False
    )
    embed.add_field(
        name="Bina Komudu İle En Uygun Haneyi Seçmek",
        value="**'!bina'** komudunu kullanarak sana en uygun olan haneyi seçebilirsin! :man_mage_tone2:",
        inline=False
    )
    embed.set_footer(text='❁ ┃ Harry Potter Roleplay')
    await ctx.send(embed=embed)


istanbul_zaman = pytz.timezone("Europe/Istanbul")
istanbul_tarih = datetime.datetime.now(istanbul_zaman)
tarih = istanbul_tarih.strftime("%d/%m/%Y %H.%M.%S")

@bot.command()
async def mesajsil(ctx, amount=0):
    if amount <= 0:
        embed = discord.Embed(description="Lütfen silmek istediğiniz mesaj sayısını giriniz.", color=0x9932CC)
        await ctx.send(embed=embed)
    else:
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f'{ctx.author.mention} tarafından, "{amount}" değerinde mesaj silindi.', delete_after=5)

#Kayıt
@bot.tree.command(name="kayıt", description="Etiketlediğiniz üye için kayıt menüsünü açar.")
@app_commands.describe(member = "Kaydı yapılacak üyeyi etiketleyiniz.")
@app_commands.describe(isim = "etiketlediğiniz üyenin ismini giriniz.")
@app_commands.describe(yas = "etiketlediğiniz üyenin yaşını giriniz.")
async def kayit(interaction: discord.Interaction, member: discord.Member, isim: str, yas: int):
    istanbul_zaman2 = pytz.timezone("Europe/Istanbul")
    istanbul_tarih2 = datetime.datetime.now(istanbul_zaman2)
    tarih2 = istanbul_tarih2.strftime("%d/%m/%Y")
    role = interaction.guild.get_role(kayit_yetkili)
    role2 = interaction.guild.get_role(erkek_rol_id)
    role3 = interaction.guild.get_role(kiz_rol_id)
    member2 = member.id
    hex = {"Member_id": member2}
    hex2 = {"Staff_id": interaction.user.id}
    hex3 = {"$inc": {"Man_reg": +1}}
    hex4 = {"$inc": {"Woman_reg": +1}}
    hex5 = {"$inc": {"Total_reg": +1}}
    user_list = db.user_info.find(hex)
    mes = '\nKayıt datası:'
    for i in user_list:
        mes = mes + '\n' + i['Nick'] + ', ' + i['Sex'] + ', ' + i['Date'] + '\n-----------------------------'
    # Belirli rollerin ID'lerini bir liste olarak tanımlayalım
    izinli_rolller = [1120816848863252597, 1120816848875827215, 1120816848875827212]

    # Kullanıcının herhangi bir izinli rolü var mı kontrol edelim
    if role.id not in izinli_rolller:
        embed = discord.Embed(
            title="Erişim Reddedildi",
            description=f'{interaction.user.mention} Bu komutu kullanma iznin yok.',
            colour=discord.Colour.red()
        )
        await interaction.response.send_message(f'{interaction.user.mention}', embed=embed)
    elif interaction.channel_id != kayit_kanal_id:
        await interaction.response.send_message(f'Lütfen üylerin kayıt işlemlerini <#{kayit_kanal_id}> kanalından yapınız', ephemeral=True)
    elif db.black_list.count_documents(hex) > 0:
        await interaction.response.send_message(f'{member.mention} üyesi kara listede olduğu için kaydı yapılamıyor.', ephemeral=True)
    elif interaction.user.id == member.id:
        await interaction.response.send_message(f'{interaction.user.mention} Kendini kayıt edemezsin.', ephemeral=True)
    elif db.rules_acpt.count_documents(hex) < 1:
        await interaction.response.send_message(f'{member.mention} üyesi sunucunun kurallarını henüz kabul etmediği içinn kayıtı yapılamıyor lütfen üyeye ``/kurallar`` komutunu kullanmasını söyleyiniz', ephemeral=True)
    elif role2 in member.roles:
        await interaction.response.send_message(f'{member.mention} üyesi zaten kayıtlı', ephemeral=True)
    elif role3 in member.roles:
        await interaction.response.send_message(f'{member.mention} üyesi zaten kayıtlı', ephemeral=True)
    elif yas < min_age:
        await interaction.response.send_message(f'{member.mention} üyesi {min_age} yaşından küçük olduğu için kayıt işlemi başarısız oldu', ephemeral=True)
    else:
        button1 = Button(label="Erkek", style=discord.ButtonStyle.blurple, custom_id="erkek", emoji="🙎")
        button2 = Button(label="Kız", style=discord.ButtonStyle.green, custom_id="kadın", emoji="👩")
        button3 = Button(label="İptal et", style=discord.ButtonStyle.red, custom_id="iptal", emoji="❌")

        async def button1_callback(interaction):
            role = interaction.guild.get_role(erkek_rol_id)
            role2 = interaction.guild.get_role(kayitsiz_rol_id)
            role3 = interaction.guild.get_role(supheli_rol_id)
            log_ch = interaction.guild.get_channel(log_kanal_id)
            g_channel = interaction.guild.get_channel(genel_chat_id)
            nick = (f'{isim} | {yas}')
            kayit_embed = discord.Embed(
                title = "Kayıt işlemi başarılı",
                description = f'``{member}`` adlı kullanıcı ``{nick}`` adıyla erkek olarak kaydedildi\nüyeye <@&{erkek_rol_id}> rolünü verdim.',
                colour = discord.Colour.green()
            )
            log_embed = discord.Embed(
                title = "Bir kayıt işlemi yapıldı",
                description = f'● Kayıt yetkilisi: ``{interaction.user}``\n● Kayıt yetkilisi id: ``{interaction.user.id}``\n● Kayıt olan üye: ``{member}``\n● Kayıt olan üye id: ``{member.id}``\n● Kayıt yapılan ad: ``{nick}``\n● Cinsiyet: ``Erkek``\n● Kayıt tarihi: ``{tarih}``',
                colour = discord.Colour.blue()
            )
            await member.add_roles(role)
            await member.remove_roles(role2)
            await member.remove_roles(role3)
            await member.edit(nick=nick)
            await interaction.response.edit_message(embed=kayit_embed, view=None)
            await log_ch.send(embed=log_embed)
            await g_channel.send(f'{member.mention} üyesi aramıza katıldı ona selam verin!')
            db.user_info.insert_one(
                {
                    "Staff_id": interaction.user.id,
                    "Member_id": member.id,
                    "Sex": "erkek",
                    "Nick": nick,
                    "Date": tarih2,
                }
            )
            await interaction.channel.send(f'{member.mention} üyesi dataya kaydedildi')
            if db.register_data.count_documents(hex2) == 0:
                    db.register_data.insert_one(
                        {
                            "Staff_id": interaction.user.id,
                            "Total_reg": 1,
                            "Man_reg": 1,
                            "Woman_reg": 0,
                            "Status": "open",
                        }
                    )
            elif db.register_data.count_documents(hex2) > 0:
                db.register_data.update_one(hex2, hex3)
                db.register_data.update_one(hex2, hex5) 
            
        async def button2_callback(interaction):
            role = interaction.guild.get_role(kiz_rol_id)
            role2 = interaction.guild.get_role(kayitsiz_rol_id)
            role3 = interaction.guild.get_role(supheli_rol_id)
            log_ch = interaction.guild.get_channel(log_kanal_id)
            g_channel = interaction.guild.get_channel(genel_chat_id)
            nick = (f'{isim} | {yas}')
            kayit_embed = discord.Embed(
                title = "Kayıt işlemi başarılı",
                description = f'``{member}`` adlı kullanıcı ``{nick}`` adıyla Kız olarak kaydedildi\nüyeye <@&{kiz_rol_id}> rolünü verdim.',
                colour = discord.Colour.green()
            )
            log_embed = discord.Embed(
                title = "Bir kayıt işlemi yapıldı",
                description = f'● Kayıt yetkilisi: ``{interaction.user}``\n● Kayıt yetkilisi id: ``{interaction.user.id}``\n● Kayıt olan üye: ``{member}``\n● Kayıt olan üye id: ``{member.id}``\n● Kayıt yapılan ad: ``{nick}``\n● Cinsiyet: ``Kız``\n● Kayıt tarihi: ``{tarih}``',
                colour = discord.Colour.blue()
            )
            await member.add_roles(role)
            await member.remove_roles(role2)
            await member.remove_roles(role3)
            await member.edit(nick=nick)
            await interaction.response.edit_message(embed=kayit_embed, view=None)
            await log_ch.send(embed=log_embed)
            await g_channel.send(f'{member.mention} üyesi aramıza katıldı ona selam verin!')
            db.user_info.insert_one(
                {
                    "Staff_id": interaction.user.id,
                    "Member_id": member.id,
                    "Sex": "kız",
                    "Nick": nick,
                    "Date": tarih2,
                }
            )
            await interaction.channel.send(f'{member.mention} üyesi dataya kaydedildi')
            if db.register_data.count_documents(hex2) == 0:
                    db.register_data.insert_one(
                        {
                            "Staff_id": interaction.user.id,
                            "Total_reg": 1,
                            "Man_reg": 0,
                            "Woman_reg": 1,
                            "Status": "open",
                        }
                    )
            elif db.register_data.count_documents(hex2) > 0:
                db.register_data.update_one(hex2, hex4)
                db.register_data.update_one(hex2, hex5) 

        async def button3_callback(interaction):
            iptal_embed = discord.Embed(
                title = "Kayıt iptal edildi",
                description = f'{member.mention} kullanıcısının kayıt işlemi iptal edildi.',
                colour = discord.Colour.red()
            )
            await interaction.response.edit_message(embed=iptal_embed, view=None)
        

        button1.callback = button1_callback
        button2.callback = button2_callback
        button3.callback = button3_callback

        view = View(timeout=60)
        view.add_item(button1)
        view.add_item(button2)
        view.add_item(button3)
        leo_register_embed = discord.Embed(
            title = "Harry Potter Magic Register System",
            description = f'Lütfen etiketlediğin üyenin cinsiyetini seç.``{mes}``',
            colour = discord.Colour.random()
        )
        leo_register_embed.set_footer(text=f'1 dakika içerisinde butonlar deaktif hale gelecektir\n{footer}')
        await interaction.response.send_message(embed=leo_register_embed, view=view, ephemeral=True)

#topr
@bot.tree.command(name="topr", description="Kayıt verilerine göre sıralama yapar")
async def topr(interaction: discord.Interaction):
    istanbul_zaman2 = pytz.timezone("Europe/Istanbul")
    istanbul_tarih2 = datetime.datetime.now(istanbul_zaman2)
    tarih2 = istanbul_tarih2.strftime("%d/%m/%Y")
    mes = 'Kayıt verileri'
    hex = {"Status": "open"}
    bos = []
    bos2 = []
    user = str(interaction.user.id)
    reg_list = db.register_data.find(hex).sort("Total_reg", -1)
    if db.register_data.count_documents(hex) == 0:
        await interaction.response.send_message("Kayıt verisi sıfırlandığı için sıralama başarısız")
    elif db.register_data.count_documents(hex) == 1:
        for i in reg_list:
            kayit_sayi = str(i['Total_reg'])
            staff = str(i['Staff_id'])
            bos.append(kayit_sayi)
            bos2.append(staff)
        if user in bos2:  
            embed = discord.Embed(
                title = "Top 1",
                description = f'1. <@{bos2[0]}>: {bos[0]} \n\n{interaction.user.mention}: {bos2.index(user)+1}. sıradasın',
                colour = discord.Colour.random()
            )
            embed.set_footer(text=f'Komutu kullanan kişi: {interaction.user}  \n{tarih2}')
            await interaction.response.send_message(embed=embed)
        elif user not in bos2:
            embed = discord.Embed(
                title = "Top 1",
                description = f'1. <@{bos2[0]}>: {bos[0]} \n\n{interaction.user.mention}: kayıt verilerin bulunamadığı için sıran tespit edilemedi',
                colour = discord.Colour.random()
            )
            embed.set_footer(text=f'Komutu kullanan kişi: {interaction.user}  \n{tarih2}')
            await interaction.response.send_message(embed=embed)
    elif db.register_data.count_documents(hex) == 2:
        for i in reg_list:
            kayit_sayi = str(i['Total_reg'])
            staff = str(i['Staff_id'])
            bos.append(kayit_sayi)
            bos2.append(staff)
        if user in bos2:  
            embed = discord.Embed(
                title = "top 2",
                description = f'1. <@{bos2[0]}>: {bos[0]} \n2. <@{bos2[1]}>: {bos[1]} \n\n{interaction.user.mention}: {bos2.index(user)+1}. sıradasın',
                colour = discord.Colour.random()
            )
            embed.set_footer(text=f'Komutu kullanan kişi: {interaction.user}  \n{tarih2}')
            await interaction.response.send_message(embed=embed)
        elif user not in bos2:
            embed = discord.Embed(
                title = "top 2",
                description = f'1. <@{bos2[0]}>: {bos[0]} \n2. <@{bos2[1]}>: {bos[1]} \n\n{interaction.user.mention}: kayıt verilerin bulunamadığı için sıran tespit edilemedi',
                colour = discord.Colour.random()
            )
            embed.set_footer(text=f'Komutu kullanan kişi: {interaction.user}  \n{tarih2}')
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("Bir hata var")
    elif db.register_data.count_documents(hex) == 3:
        for i in reg_list:
            kayit_sayi = str(i['Total_reg'])
            staff = str(i['Staff_id'])
            bos.append(kayit_sayi)
            bos2.append(staff)
        if user in bos2:  
            embed = discord.Embed(
                title = "top 3",
                description = f'1. <@{bos2[0]}>: {bos[0]} \n2. <@{bos2[1]}>: {bos[1]} \n3. <@{bos2[2]}>: {bos[2]} \n\n{interaction.user.mention}: {bos2.index(user)+1}. sıradasın',
                colour = discord.Colour.random()
            )
            embed.set_footer(text=f'Komutu kullanan kişi: {interaction.user}  \n{tarih2}')
            await interaction.response.send_message(embed=embed)
        elif user not in bos2:
            embed = discord.Embed(
                title = "top 3",
                description = f'1. <@{bos2[0]}>: {bos[0]} \n2. <@{bos2[1]}>: {bos[1]} \n3. <@{bos2[2]}>: {bos[2]} \n\n{interaction.user.mention}: kayıt verilerin bulunamadığı için sıran tespit edilemedi',
                colour = discord.Colour.random()
            )
            embed.set_footer(text=f'Komutu kullanan kişi: {interaction.user}  \n{tarih2}')
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("Bir hata var")
    elif db.register_data.count_documents(hex) == 4:
        for i in reg_list:
            kayit_sayi = str(i['Total_reg'])
            staff = str(i['Staff_id'])
            bos.append(kayit_sayi)
            bos2.append(staff)
        if user in bos2:  
            embed = discord.Embed(
                title = "top 4",
                description = f'1. <@{bos2[0]}>: {bos[0]} \n2. <@{bos2[1]}>: {bos[1]} \n3. <@{bos2[2]}>: {bos[2]} \n4. <@{bos2[3]}>: {bos[3]} \n\n{interaction.user.mention}: {bos2.index(user)+1}. sıradasın',
                colour = discord.Colour.random()
            )
            embed.set_footer(text=f'Komutu kullanan kişi: {interaction.user}  \n{tarih2}')
            await interaction.response.send_message(embed=embed)
        elif user not in bos2:
            embed = discord.Embed(
                title = "top 4",
                description = f'1. <@{bos2[0]}>: {bos[0]} \n2. <@{bos2[1]}>: {bos[1]} \n3. <@{bos2[2]}>: {bos[2]} \n4. <@{bos2[3]}>: {bos[3]} \n\n{interaction.user.mention}: kayıt verilerin bulunamadığı için sıran tespit edilemedi',
                colour = discord.Colour.random()
            )
            embed.set_footer(text=f'Komutu kullanan kişi: {interaction.user}  \n{tarih2}')
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("Bir hata var")
    elif db.register_data.count_documents(hex) >= 5:
        for i in reg_list:
            kayit_sayi = str(i['Total_reg'])
            staff = str(i['Staff_id'])
            bos.append(kayit_sayi)
            bos2.append(staff)
        if user in bos2:  
            embed = discord.Embed(
                title = "top 5",
                description = f'1. <@{bos2[0]}>: {bos[0]} \n2. <@{bos2[1]}>: {bos[1]} \n3. <@{bos2[2]}>: {bos[2]} \n4. <@{bos2[3]}>: {bos[3]} \n5. <@{bos2[4]}>: {bos[4]}\n{interaction.user.mention}: {bos2.index(user)+1}. sıradasın',
                colour = discord.Colour.random()
            )
            embed.set_footer(text=f'Komutu kullanan kişi: {interaction.user}  \n{tarih2}')
            await interaction.response.send_message(embed=embed)
        elif user not in bos2:
            embed = discord.Embed(
                title = "top 5",
                description = f'1. <@{bos2[0]}>: {bos[0]} \n2. <@{bos2[1]}>: {bos[1]} \n3. <@{bos2[2]}>: {bos[2]} \n4. <@{bos2[3]}>: {bos[3]} \n5. <@{bos2[4]}>: {bos[4]}\n{interaction.user.mention}: kayıt verilerin bulunamadığı için sıran tespit edilemedi',
                colour = discord.Colour.random()
            )
            embed.set_footer(text=f'Komutu kullanan kişi: {interaction.user}  \n{tarih2}')
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("Bir hata var")
    else:
        embed = discord.Embed(
            title = "Bir hata var",
            description = "Tespit edilemeyen bir hata oldu lütfen daha sonra tekrar deneyiniz.",
            colour = discord.Colour.red()
        )
        await interaction.response.send_message(embed=embed)

#rstat
@bot.tree.command(name="rstat", description="Etiketlediğiniz üyenin ya da sizin kayıt verilerini gösterir.")
@app_commands.describe(member = "istatistiği görüntülenecek kullanıcıyı seçin")
async def rstat(interaction: discord.Interaction, member: discord.Member=None):
    istanbul_zaman2 = pytz.timezone("Europe/Istanbul")
    istanbul_tarih2 = datetime.datetime.now(istanbul_zaman2)
    tarih2 = istanbul_tarih2.strftime("%d/%m/%Y")
    role = interaction.guild.get_role(kayit_yetkili)
    # Belirli rollerin ID'lerini bir liste olarak tanımlayalım
    izinli_rolller = [1120816848863252597, 1120816848875827215, 1120816848875827212]

    # Kullanıcının herhangi bir izinli rolü var mı kontrol edelim
    if role.id not in izinli_rolller:
        embed = discord.Embed(
            title="Erişim Reddedildi",
            description=f'{interaction.user.mention} Bu komutu kullanma iznin yok.',
            colour=discord.Colour.red()
        )
        await interaction.response.send_message(f'{interaction.user.mention}', embed=embed)
    elif role in interaction.user.roles:
        if member == None:
            member = interaction.user
        member2 = member.id
        hex = {"Staff_id": member2}
        staff_list = db.register_data.find(hex)
        if db.register_data.count_documents(hex) == 0:
            embed = discord.Embed(
                title = "Veri bulunamadı",
                description = f'{member} kullanıcısının kayıt verileri bulunamadı',
                colour = discord.Colour.red()
            )
            embed.set_footer(text=f'Komutu kullanan kişi: {interaction.user}  \n{tarih2}')
            await interaction.response.send_message(embed=embed, ephemeral=True)
        elif db.register_data.count_documents(hex) == 1:
            for i in staff_list:
                embed = discord.Embed(
                    title = f'Kayıt verileri sıralandı',
                    description = f'**{member} yetkilisinin kayıt verileri**\n\nToplam kayıt: ' + str(i['Total_reg']) + '\nErkek kayıt: ' + str(i['Man_reg']) + '\nKız kayıt: ' + str(i['Woman_reg']),
                    colour = discord.Colour.random()
                )
                embed.set_footer(text=f'Komutu kullanan kişi: {interaction.user}  \n{tarih2}')
                await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message("Bir hata var", ephemeral=True)

#black list
@bot.tree.command(name="blacklist", description="Etiketlediğini üyeyi kara listeye ekler/çıkarır")
@app_commands.describe(member = "işlem yapılacak üyeyi etiketleyiniz.")
@app_commands.describe(sebep = "Bir sebep giriniz")
async def blacklist(interaction: discord.Interaction, member: discord.Member, sebep: str="Sebep belirtilmedi"):
    istanbul_zaman2 = pytz.timezone("Europe/Istanbul")
    istanbul_tarih2 = datetime.datetime.now(istanbul_zaman2)
    tarih2 = istanbul_tarih2.strftime("%d/%m/%Y")
    role = interaction.guild.get_role(yonetici_id)
    log_ch = interaction.guild.get_channel(bl_log_kanal_id)
    member2 = member.id
    hex = {"Member_id": member2}
    if role not in interaction.user.roles:
        embed = discord.Embed(
            title = "Erişim reddedildi",
            description = "Bu komutu kullanmak için yeterli izinlere sahip değilsin",
            colour = discord.Colour.red()
        )
        embed.set_footer(text=f'Komutu kullanan kişi: {interaction.user}  \n{tarih2}')
        await interaction.response.send_message(embed=embed)
        await log_ch.send(embed=embed)
    elif db.black_list.count_documents(hex) > 0:
        button1 = Button(label="Onayla", style=discord.ButtonStyle.green, custom_id="onay", emoji="✔️")
        button2 = Button(label="İptal et", style=discord.ButtonStyle.red, custom_id="iptal", emoji="❌")
        async def button1_callback(interaction):
            db.black_list.delete_one(hex)
            embed = discord.Embed(
                title = "İşlem başarılı",
                description = f'{member.mention} **üyesi artık kara listede değil**\n\n● Yetkili id: {interaction.user.id}\n● Üye id: {member.id}\n● Sebep: {sebep}\n● Tarih: {tarih2}',
                colour = discord.Colour.green()
            )
            embed.set_footer(text=f'Komutu kullanan kişi: {interaction.user}  \n{tarih2}')
            await interaction.response.edit_message(embed=embed, view=None)
            await log_ch.send(embed=embed)
        
        async def button2_callback(interaction):
            embed = discord.Embed(
                title = "İşlem iptal edildi",
                description = "Black list işlemi iptal edildi",
                colour = discord.Colour.red()
            )
            await interaction.response.edit_message(embed=embed, view=None)
        
        button1.callback = button1_callback
        button2.callback = button2_callback

        view = View(timeout=60)
        view.add_item(button1)
        view.add_item(button2)
        leo_bl_embed = discord.Embed(
            title = "Harry Potter Magic black list system",
            description = f'{member.mention} üyesini kara listeden çıkarmak istediğine emin misin?\n\nİşlemi onaylıyorsan yeşil butona bas\nİşlemi iptal etmek istiyorsan kırmızı butona bas',
            colour = discord.Colour.random()
        )
        leo_bl_embed.set_footer(text=f'1 dakika içerisinde butonlar deaktif hale gelecektir\n{footer}')
        await interaction.response.send_message(embed=leo_bl_embed, view=view, ephemeral=True)
            
    elif db.black_list.count_documents(hex) == 0:
        button1 = Button(label="Onayla", style=discord.ButtonStyle.green, custom_id="onay", emoji="✔️")
        button2 = Button(label="İptal et", style=discord.ButtonStyle.red, custom_id="iptal", emoji="❌")
        async def button1_callback(interaction):
            db.black_list.insert_one(
                {
                    "Staff_id": interaction.user.id,
                    "Member_id": member2,
                    "Reason": sebep,
                    "Date": tarih2,
                }
            )
            embed = discord.Embed(
                title = "İşlem başarılı",
                description = f'{member.mention} **üyesi artık kara listede**\n\n● Yetkili id: {interaction.user.id}\n● Üye id: {member.id}\n● Sebep: {sebep}\n● Tarih: {tarih2}',
                colour = discord.Colour.red()
            )
            embed.set_footer(text=f'Komutu kullanan kişi: {interaction.user}  \n{tarih2}')
            await interaction.response.edit_message(embed=embed, view=None)
            await log_ch.send(embed=embed)
        
        async def button2_callback(interaction):
            embed = discord.Embed(
                title = "İşlem iptal edildi",
                description = "Black list işlemi iptal edildi",
                colour = discord.Colour.red()
            )
            await interaction.response.edit_message(embed=embed, view=None)

        button1.callback = button1_callback
        button2.callback = button2_callback

        view = View(timeout=60)
        view.add_item(button1)
        view.add_item(button2)
        leo_bl_embed = discord.Embed(
            title = "Leo black list system",
            description = f'{member.mention} üyesini kara listeye almak istediğine emin misin?\n\nİşlemi onaylıyorsan yeşil butona bas\nİşlemi iptal etmek istiyorsan kırmızı butona bas',
            colour = discord.Colour.random()
        )
        leo_bl_embed.set_footer(text=f'1 dakika içerisinde butonlar deaktif hale gelecektir\n{footer}')
        await interaction.response.send_message(embed=leo_bl_embed, view=view, ephemeral=True)

    else:
        print("bl komutunda bir şeyler ters gitti")


@bot.tree.command(name="data", description="Etiketlediğiniz üyeyin kayıt geçmişini gösterir")
@app_commands.describe(member="işlem yapılacak üyeyi etiketleyiniz.")
async def data(interaction: discord.Interaction, member: discord.Member):
    istanbul_zaman2 = pytz.timezone("Europe/Istanbul")
    istanbul_tarih2 = datetime.datetime.now(istanbul_zaman2)
    tarih2 = istanbul_tarih2.strftime("%d/%m/%Y")
    role = interaction.guild.get_role(kayit_yetkili)
    member2 = member.id
    hex = {"Member_id": member2}
    mes = 'Daha önceki isimleri'
    user_list = db.user_info.find(hex)
    # Belirli rollerin ID'lerini bir liste olarak tanımlayalım
    izinli_rolller = [1120816848863252597, 1120816848875827215, 1120816848875827212]

    # Kullanıcının herhangi bir izinli rolü var mı kontrol edelim
    if role.id not in izinli_rolller:
        embed = discord.Embed(
            title="Erişim Reddedildi",
            description=f'{interaction.user.mention} Bu komutu kullanma iznin yok.',
            colour=discord.Colour.red()
        )
        embed.set_footer(text=f'Komutu kullanan kişi: {interaction.user}  \n{tarih2}')
        await interaction.response.send_message(f'{interaction.user.mention}', embed=embed)
    elif db.user_info.count_documents(hex) == 0:
        embed = discord.Embed(
            title="Veri bulunamadı",
            description=f'{member.mention} üyesinin kayıtlı isim geçmişi bulunamadı',
            colour=discord.Colour.red()
        )
        embed.set_footer(text=f'Komutu kullanan kişi: {interaction.user}  \n{tarih2}')
        await interaction.response.send_message(embed=embed)

    elif db.user_info.count_documents(hex) != 0:
        for i in user_list:
            mem = str(i['Staff_id'])
            mes = mes + '\n' + i['Nick'] + ',  ``' + i['Date'] + '``,  **' + i['Sex'] + '**,  ' + '<@' + mem + '>'
            embed = discord.Embed(
                title = "Kullanıcının önceki isimleri",
                description = f'**{member.mention} kullanıcısının daha önceki isimleri**\n{mes}',
                colour = discord.Colour.red()
            )
            embed.set_footer(text=f'Komutu kullanan kişi: {interaction.user}  \n{tarih2}')
        await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message("Bilinmeyen bir hata oluştu")

#kayit sifirla
@bot.tree.command(name="kayıtres", description="Etiketlediğiniz yetkilinin kayıt ettiği kişi sayısını sıfırlar")
@app_commands.describe(member = "işlem yapılacak yetkiliyi etiketleyiniz.")
async def kayitres(interaction: discord.Interaction, member: discord.Member):
    istanbul_zaman2 = pytz.timezone("Europe/Istanbul")
    istanbul_tarih2 = datetime.datetime.now(istanbul_zaman2)
    tarih2 = istanbul_tarih2.strftime("%d/%m/%Y")
    role = interaction.guild.get_role(yonetici_id)
    log_ch = interaction.guild.get_channel(data_log_kanal_id)
    member2 = member.id
    hex = {"Staff_id": member2}
    if role not in interaction.user.roles:
        embed = discord.Embed(
            title = "Erişim Reddedildi",
            description = f'{interaction.user.mention} Bu komutu kullanma iznin yok.',
            colour = discord.Colour.red()
        )
        embed.set_footer(text=f'Komutu kullanan kişi: {interaction.user}  \n{tarih2}')
        await interaction.response.send_message(embed=embed)
    elif db.register_data.count_documents(hex) == 1:
        button1 = Button(label="Onayla", style=discord.ButtonStyle.green, custom_id="onay", emoji="✔️")
        button2 = Button(label="İptal et", style=discord.ButtonStyle.red, custom_id="iptal", emoji="❌")
        async def button1_callback(interaction):
            db.register_data.delete_one(hex)
            embed = discord.Embed(
                title = "İşlem başarılı",
                description = f'{interaction.user.mention} tarafından {member.mention} üyesinin **kayıt sayısı** sıfırlandı',
                colour = discord.Colour.green()
            )
            embed.set_footer(text=f'Komutu kullanan kişi: {interaction.user}  \n{tarih2}')
            await interaction.response.edit_message(embed=embed, view=None)
            await log_ch.send(embed=embed)

        async def button2_callback(interaction):
            embed = discord.Embed(
                title = "İşlem iptal edildi",
                description = "Kayıt sıfırlama işlemi iptal edildi",
                colour = discord.Colour.red()
            )
            await interaction.response.edit_message(embed=embed, view=None)

        button1.callback = button1_callback
        button2.callback = button2_callback

        view = View(timeout=60)
        view.add_item(button1)
        view.add_item(button2)
        leo_kres_embed = discord.Embed(
            title = "Harry Potter RolePlay System",
            description = f'{member.mention} üyesinin kayıt sayısını sıfırlamak istediğine emin misin?\n\nİşlemi onaylıyorsan yeşil butona bas\nİşlemi iptal etmek istiyorsan kırmızı butona bas',
            colour = discord.Colour.random()
        )
        leo_kres_embed.set_footer(text=f'1 dakika içerisinde butonlar deaktif hale gelecektir\n{footer}')
        await interaction.response.send_message(embed=leo_kres_embed, view=view, ephemeral=True)

    elif db.register_data.count_documents(hex) == 0:
        embed = discord.Embed(
            title = "İşlem başarılı",
            description = f'{member.mention} üyesinin kayıt sayısı zaten daha önceden sıfırlandı',
            colour = discord.Colour.red()
        )
        embed.set_footer(text=f'Komutu kullanan kişi: {interaction.user}  \n{tarih2}')
        await interaction.response.send_message(embed=embed)
    elif db.register_data.count_documents(hex) > 1:
        button1 = Button(label="Onayla", style=discord.ButtonStyle.green, custom_id="onay", emoji="✔️")
        button2 = Button(label="İptal et", style=discord.ButtonStyle.red, custom_id="iptal", emoji="❌")
        async def button1_callback(interaction):
            db.register_data.delete_many(hex)
            embed = discord.Embed(
                title = "İşlem başarılı",
                description = f'{interaction.user.mention} tarafından {member.mention} üyesinin **kayıt sayısı** sıfırlandı',
                colour = discord.Colour.green()
            )
            embed.set_footer(text=f'Komutu kullanan kişi: {interaction.user}  \n{tarih2}')
            await interaction.response.edit_message(embed=embed, view=None)
            await log_ch.send(embed=embed)

        async def button2_callback(interaction):
            embed = discord.Embed(
                title = "İşlem iptal edildi",
                description = "Kayıt sıfırlama işlemi iptal edildi",
                colour = discord.Colour.red()
            )
            await interaction.response.edit_message(embed=embed, view=None)

        button1.callback = button1_callback
        button2.callback = button2_callback

        view = View(timeout=60)
        view.add_item(button1)
        view.add_item(button2)
        leo_kres_embed = discord.Embed(
            title = "Leo system",
            description = f'{member.mention} üyesinin kayıt sayısını sıfırlamak istediğine emin misin?\n\nİşlemi onaylıyorsan yeşil butona bas\nİşlemi iptal etmek istiyorsan kırmızı butona bas',
            colour = discord.Colour.random()
        )
        leo_kres_embed.set_footer(text=f'1 dakika içerisinde butonlar deaktif hale gelecektir\n{footer}')
        await interaction.response.send_message(embed=leo_kres_embed, view=view, ephemeral=True)
    else:
        await interaction.response.send_message("Bir hata var", ephemeral=True)

#isim geçmişi sıfırla
@bot.tree.command(name="isimres", description="Etiketlediğiniz kişinin isim geçmişini sıfırlar")
@app_commands.describe(member = "işlem yapılacak yetkiliyi etiketleyiniz.")
async def isimres(interaction: discord.Interaction, member: discord.Member):
    istanbul_zaman2 = pytz.timezone("Europe/Istanbul")
    istanbul_tarih2 = datetime.datetime.now(istanbul_zaman2)
    tarih2 = istanbul_tarih2.strftime("%d/%m/%Y")
    role = interaction.guild.get_role(yonetici_id)
    log_ch = interaction.guild.get_channel(data_log_kanal_id)
    member2 = member.id
    hex = {"Member_id": member2}
    if role not in interaction.user.roles:
        embed = discord.Embed(
            title = "Erişim Reddedildi",
            description = f'{interaction.user.mention} Bu komutu kullanma iznin yok.',
            colour = discord.Colour.red()
        )
        embed.set_footer(text=f'Komutu kullanan kişi: {interaction.user}  \n{tarih2}')
        await interaction.response.send_message(embed=embed)
    elif db.user_info.count_documents(hex) == 1:
        button1 = Button(label="Onayla", style=discord.ButtonStyle.green, custom_id="onay", emoji="✔️")
        button2 = Button(label="İptal et", style=discord.ButtonStyle.red, custom_id="iptal", emoji="❌")
        async def button1_callback(interaction):
            db.user_info.delete_one(hex)
            embed = discord.Embed(
                title = "İşlem başarılı",
                description = f'{interaction.user.mention} tarafından {member.mention} üyesinin **isim geçmişi** sıfırlandı',
                colour = discord.Colour.green()
            )
            embed.set_footer(text=f'Komutu kullanan kişi: {interaction.user}  \n{tarih2}')
            await interaction.response.edit_message(embed=embed, view=None)
            await log_ch.send(embed=embed)

        async def button2_callback(interaction):
            embed = discord.Embed(
                title = "İşlem iptal edildi",
                description = "İsim sıfırlama işlemi iptal edildi",
                colour = discord.Colour.red()
            )
            await interaction.response.edit_message(embed=embed, view=None)

        button1.callback = button1_callback
        button2.callback = button2_callback

        view = View(timeout=60)
        view.add_item(button1)
        view.add_item(button2)
        leo_kres_embed = discord.Embed(
            title = "Leo system",
            description = f'{member.mention} üyesinin isim geçmişini sıfırlamak istediğine emin misin?\n\nİşlemi onaylıyorsan yeşil butona bas\nİşlemi iptal etmek istiyorsan kırmızı butona bas',
            colour = discord.Colour.random()
        )
        leo_kres_embed.set_footer(text=f'1 dakika içerisinde butonlar deaktif hale gelecektir\n{footer}')
        await interaction.response.send_message(embed=leo_kres_embed, view=view, ephemeral=True)

    elif db.user_info.count_documents(hex) == 0:
        db.user_info.delete_one(hex)
        embed = discord.Embed(
            title = "İşlem başarılı",
            description = f'{member.mention} üyesinin kayıtlı isim geçmişi bulunamadı',
            colour = discord.Colour.red()
        )
        embed.set_footer(text=f'Komutu kullanan kişi: {interaction.user}  \n{tarih2}')
        await interaction.response.send_message(embed=embed)
    elif db.user_info.count_documents(hex) > 1:
        button1 = Button(label="Onayla", style=discord.ButtonStyle.green, custom_id="onay", emoji="✔️")
        button2 = Button(label="İptal et", style=discord.ButtonStyle.red, custom_id="iptal", emoji="❌")
        async def button1_callback(interaction):
            db.user_info.delete_many(hex)
            embed = discord.Embed(
                title = "İşlem başarılı",
                description = f'{interaction.user.mention} tarafından {member.mention} üyesinin **isim geçmişi** sıfırlandı',
                colour = discord.Colour.green()
            )
            embed.set_footer(text=f'Komutu kullanan kişi: {interaction.user}  \n{tarih2}')
            await interaction.response.edit_message(embed=embed, view=None)
            await log_ch.send(embed=embed)

        async def button2_callback(interaction):
            embed = discord.Embed(
                title = "İşlem iptal edildi",
                description = "İsim sıfırlama işlemi iptal edildi",
                colour = discord.Colour.red()
            )
            await interaction.response.edit_message(embed=embed, view=None)

        button1.callback = button1_callback
        button2.callback = button2_callback

        view = View(timeout=60)
        view.add_item(button1)
        view.add_item(button2)
        leo_kres_embed = discord.Embed(
            title = "Leo system",
            description = f'{member.mention} üyesinin isim geçmişini sıfırlamak istediğine emin misin?\n\nİşlemi onaylıyorsan yeşil butona bas\nİşlemi iptal etmek istiyorsan kırmızı butona bas',
            colour = discord.Colour.random()
        )
        leo_kres_embed.set_footer(text=f'1 dakika içerisinde butonlar deaktif hale gelecektir\n{footer}')
        await interaction.response.send_message(embed=leo_kres_embed, view=view, ephemeral=True)

#kurallar
@bot.tree.command(name="kurallar", description="Sunucunun kurallarını görüntülemenizi sağlar")
async def kurallar(interaction: discord.Interaction):
    istanbul_zaman2 = pytz.timezone("Europe/Istanbul")
    istanbul_tarih2 = datetime.datetime.now(istanbul_zaman2)
    tarih2 = istanbul_tarih2.strftime("%d/%m/%Y")
    role = interaction.guild.get_role(yonetici_id)
    log_ch = interaction.guild.get_channel(kurallar_kanal_id)
    hex = {"Member_id": interaction.user.id}
    accept_list = db.rules_acpt.find(hex)
    if db.rules_acpt.count_documents(hex) >= 1:
        for i in accept_list:
            mes = 'Sunucunun kurallarını zaten ``' + i['Date'] + f'`` tarihinde kabul ettin kuralları tekrar okumak istiyorsan <#{kurallar_kanal_id}> kanalına göz atabilirsin'
            embed = discord.Embed(
                title = "Sunucu kuralları",
                description = mes,
                colour = discord.Colour.red()
            )
            embed.set_footer(text=f'Komutu kullanan kişi: {interaction.user}  \n{tarih}')
        await interaction.response.send_message(embed=embed, ephemeral=True)
    elif db.rules_acpt.count_documents(hex) == 0:
        button1 = Button(label="Kabul et", style=discord.ButtonStyle.green, custom_id="kabul", emoji="✔️")
        button2 = Button(label="Reddet", style=discord.ButtonStyle.red, custom_id="red", emoji="❌")
        async def button1_callback(interaction):
            db.rules_acpt.insert_one(
                        {
                            "Member_id": interaction.user.id,
                            "Date": tarih2,
                        }
                    )
            embed = discord.Embed(
                title = "İşlem başarılı",
                description = f'Kuralları başarılı bir şekilde kabul ettin',
                colour = discord.Colour.green()
            )
            embed2 = discord.Embed(
                title = "Kurallar kabul edildi",
                description = f'● Kabul eden üye: {interaction.user.id}\n● Kabul tarihi: {tarih}',
                colour = discord.Colour.green()
            )
            await interaction.response.edit_message(embed=embed, view=None)
            await log_ch.send(embed=embed2)

        async def button2_callback(interaction):
            embed = discord.Embed(
                title = "İşlem iptal edildi",
                description = "Kuralları reddettin unutma ki sunucunun kurallarını kabul etmeden kayıt olamazsın",
                colour = discord.Colour.red()
            )
            await interaction.response.edit_message(embed=embed, view=None)

        button1.callback = button1_callback
        button2.callback = button2_callback

        view = View(timeout=60)
        view.add_item(button1)
        view.add_item(button2)
        leo_rules_embed = discord.Embed(
            title = "Harry Potter Sunucu Kuralları",
            description = f'Kuralları okumak için <#1120816850377388041> kanalına giriniz. Kuralları kabul ettim dediğiniz andan itibaren onaylamış ve okumuş kabul edileceksiniz. Kurallar dışına çıkmanız halinde alacağınız cezadan sunucumuz sorumlu değildir.',
            colour = discord.Colour.random()
        )
        leo_rules_embed.set_footer(text=f'2 dakika içerisinde butonlar deaktif hale gelecektir\n{footer}')
        await interaction.response.send_message(embed=leo_rules_embed, view=view, ephemeral=True)


@bot.event
async def on_member_join(member):
    age = member.created_at.strftime("%d/%m/%Y %H.%M.%S")
    bugün = datetime.datetime.now()
    yil = int(member.created_at.strftime("%Y"))
    ay = int(member.created_at.strftime("%m"))
    gun = int(member.created_at.strftime("%d"))
    acilis = datetime.datetime(yil, ay, gun)

    ay2 = datetime.datetime.strftime(acilis, '%B')
    fark = bugün - acilis
    bekleme_suresi = supheli_hesap_suresi - fark.days
    if fark.days < supheli_hesap_suresi:
        role = member.guild.get_role(supheli_rol_id)
        channel = member.guild.get_channel(supheli_kanal_id)
        nick = (f'Şüpheli hesap')
        embed = discord.Embed(
            title = "Şüpheli Hesap",
            description = f'● Hesap adı: ``{member}``\n● Hesap id: ``{member.id}``\n● kuruluş tarihi: ``{gun} {ay2} {yil}``\n● Geçen süre: ``{fark.days} gün``\n● Kalan süre: ``{bekleme_suresi} gün``',
            colour = discord.Colour.red()
        )
        await member.add_roles(role)
        await member.edit(nick=nick)
        await channel.send(embed=embed)
        await member.send(f'Sunucuya kayıt olmak için hesabının en az {supheli_hesap_suresi} gün önce açılmış olması lazım yani {bekleme_suresi} gün daha beklemelisin. ')
    else:
        role = member.guild.get_role(kayitsiz_rol_id)
        channel = member.guild.get_channel(hg_kanal_id)
        nick = (f'isim | yaş')
        embed = discord.Embed(
            title = "Aramıza yeni bir üye katıldı",
            description = f':tada: {member.mention} sunucumuza hoş geldin :tada: \n\nhesabının ``{gun} {ay2} {yil}`` tarihinde oluşturulmuş\n\nSunucu kurallarımıza <#{kurallar_kanal_id}> kanalından ulaşabilirsin\n\n Seninle birlikte **{member.guild.member_count}** kişiyiz. kayıt olmak için ses teyit odalarına girebilirsin <@&{kayit_yetkili}> rolüne sahip yetkililerimiz seninle ilgilenecektir! iyi eğlenceler.\n\n<#{sesli_kayit_kanal_id}> kanalına bağlanarak kayıt olabilirsin.',
            colour = discord.Colour.green()
        )
        await member.add_roles(role)
        await channel.send('<@&{}> {member.mention}',embed=embed)
        


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(bb_kanal_id)
    bb_embed = discord.Embed(
        title = "Bir üye sunucumuzdan ayrıldı",
        description = f'{member} adlı üye sunucumuzdan ayrıldı.',
        colour = discord.Colour.red()
    )
    await channel.send(embed=bb_embed)

@bot.event
async def on_presence_update(before, after):
    role = before.guild.get_role(kayitsiz_rol_id)
    channel = bot.get_channel(kayit_kanal_id)
    if role in before.roles:
        if before.status is discord.Status.offline and after.status is not discord.Status.offline:
            await channel.send(f'{before.mention} tekrardan aktif oldun ama hala kayıta gelmedin seni bekliyorum')
    else:
        pass
    
@bot.event 
async def on_ready():
    print(bot.user.name)
    print("Bot Açılma Saati: ", tarih)
    #await channel.connect()
    print("Bot sesli kanala bağlandı")
    await bot.change_presence(activity=discord.Game(name=footer))
    try:
        synced = await bot.tree.sync()
        print(f'Entegre edilen slash Komut sayısı: {len(synced)}')
    except Exception as e:
        print(e)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yapıldı.')
    print("Bot Açılma Saati: ", tarih)
    #await channel.connect()
    print("Bot sesli kanala bağlandı")
    await bot.change_presence(activity=discord.Game(name=footer))
    try:
        synced = await bot.tree.sync()
        print(f'Entegre edilen slash Komut sayısı: {len(synced)}')
    except Exception as e:
        print(e)
        
    # Hedeflenen ses kanalının ID'si
    target_channel_id = 1211039928935383200

    # Hedeflenen ses kanalı nesnesini al
    target_channel = bot.get_channel(target_channel_id)

    if target_channel:
        # Belirtilen ses kanalına katıl
        await target_channel.connect()
        print(f'Ses kanalına başarıyla katıldı: {target_channel.name}')
    else:
        print('Belirtilen ses kanalı bulunamadı.')

@bot.event
async def on_disconnect():
    print('Bot, ses kanalından ayrıldı.')

bot.run(token)
