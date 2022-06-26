# Generated by Django 3.2 on 2022-06-26 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20220626_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='sex',
            field=models.CharField(blank=True, choices=[('male', '男性'), ('female', '女性')], max_length=10, verbose_name='seibetu'),
        ),
        migrations.AlterField(
            model_name='user',
            name='kodomo',
            field=models.CharField(blank=True, choices=[('nasi', 'なし'), ('dokyo', '同居中'), ('bekkyo', '別居中')], max_length=40, verbose_name='kodomo'),
        ),
        migrations.AlterField(
            model_name='user',
            name='kyojuchi',
            field=models.CharField(blank=True, choices=[('hokkaido', '北海道'), ('aomori', '青森県'), ('iwate', '岩手県'), ('miyagi', '宮城県'), ('akita', '秋田県'), ('yamagata', '山形県'), ('hukusima', '福島県'), ('ibaraki', '茨城県'), ('tochigi', '栃木県'), ('gunma', '群馬県'), ('saitama', '埼玉県'), ('chiba', '千葉県'), ('tokyo', '東京都'), ('kanagawa', '神奈川県'), ('niigata', '新潟県'), ('toyama', '富山県'), ('isikawa', '石川県'), ('hukui', '福井県'), ('yamanasi', '山梨県'), ('nagano', '長野県'), ('gihu', '岐阜県'), ('sizuoka', '静岡県'), ('aichi', '愛知県'), ('mie', '三重県'), ('siga', '滋賀県'), ('kyoto', '京都府'), ('osaka', '大阪府'), ('hyogo', '兵庫県'), ('nara', '奈良県'), ('wakayama', '和歌山県'), ('tottori', '鳥取県'), ('simane', '島根県'), ('okayama', '岡山県'), ('hirosima', '広島県'), ('yamaguchi', '山口県'), ('tokusima', '徳島県'), ('kagawa', '香川県'), ('ehime', '愛媛県'), ('kochi', '高知県'), ('hukuoka', '福岡県'), ('saga', '佐賀県'), ('nagasaki', '長崎県('), ('kumamoto', '熊本県'), ('ooita', '大分県'), ('miyazaki', '宮崎県'), ('kagosima', '鹿児島県'), ('okinawa', '沖縄県')], max_length=40, verbose_name='kyojuchi'),
        ),
        migrations.AlterField(
            model_name='user',
            name='osake',
            field=models.CharField(blank=True, choices=[('mainichi', '毎日飲む'), ('shuichi', '週数回程度飲む'), ('tukiichi', '月数回程度飲む'), ('nomanai', '飲まない')], max_length=40, verbose_name='osake'),
        ),
        migrations.AlterField(
            model_name='user',
            name='shokugyo',
            field=models.CharField(blank=True, choices=[('eigyo', '営業'), ('', '事務・管理'), ('kikaku', '企画・マーケティング・経営・管理職'), ('sabisu', 'サービス・販売・外食'), ('ribiyo', '理美容・エステ・ネイル関係'), ('web', 'Web・インターネット・ゲーム'), ('creative', 'クリエイティブ（メディア・アパレル・デザイン）'), ('senmonshoku', '専門職（コンサルタント・士業・金融・不動産）'), ('it', 'ITエンジニア（システム開発・SE・インフラ）'), ('enjinia', 'エンジニア（機械・電気・電子・半導体・制御）'), ('sozai', '素材・化学・食品・医薬品技術職'), ('kenchiku', '建築・土木技術職'), ('ginoko', '技能工・設備・交通・運輸'), ('iryo', '医療・福祉・介護'), ('sonota', '教育・保育・公務員・農林水産・その他')], max_length=40, verbose_name='shokugyo'),
        ),
        migrations.AlterField(
            model_name='user',
            name='shumi',
            field=models.CharField(blank=True, choices=[('supotu', 'スポーツ（観覧も含む）'), ('geijutu', '美術・演劇・映画・音楽等鑑賞'), ('ongaku', '楽器演奏・カラオケ・ダンス等'), ('shodo', '書道・華道・茶道等'), ('shugei', '和裁・洋裁・手芸等'), ('ryori', '料理・菓子作り'), ('engei', '園芸・ガーデニング・畑'), ('sosaku', '日曜大工・絵画・彫刻・陶芸等'), ('shasin', '写真撮影'), ('bungei', '詩・和歌・俳句・小説'), ('dokusho', '読書'), ('game', '囲碁・将棋・ゲーム等'), ('kengaku', '動植物園・水族館等見学'), ('camp', 'キャンプ'), ('other', 'その他')], max_length=40, verbose_name='shumi'),
        ),
        migrations.AlterField(
            model_name='user',
            name='shussin',
            field=models.CharField(blank=True, choices=[('hokkaido', '北海道'), ('aomori', '青森県'), ('iwate', '岩手県'), ('miyagi', '宮城県'), ('akita', '秋田県'), ('yamagata', '山形県'), ('hukusima', '福島県'), ('ibaraki', '茨城県'), ('tochigi', '栃木県'), ('gunma', '群馬県'), ('saitama', '埼玉県'), ('chiba', '千葉県'), ('tokyo', '東京都'), ('kanagawa', '神奈川県'), ('niigata', '新潟県'), ('toyama', '富山県'), ('isikawa', '石川県'), ('hukui', '福井県'), ('yamanasi', '山梨県'), ('nagano', '長野県'), ('gihu', '岐阜県'), ('sizuoka', '静岡県'), ('aichi', '愛知県'), ('mie', '三重県'), ('siga', '滋賀県'), ('kyoto', '京都府'), ('osaka', '大阪府'), ('hyogo', '兵庫県'), ('nara', '奈良県'), ('wakayama', '和歌山県'), ('tottori', '鳥取県'), ('simane', '島根県'), ('okayama', '岡山県'), ('hirosima', '広島県'), ('yamaguchi', '山口県'), ('tokusima', '徳島県'), ('kagawa', '香川県'), ('ehime', '愛媛県'), ('kochi', '高知県'), ('hukuoka', '福岡県'), ('saga', '佐賀県'), ('nagasaki', '長崎県('), ('kumamoto', '熊本県'), ('ooita', '大分県'), ('miyazaki', '宮崎県'), ('kagosima', '鹿児島県'), ('okinawa', '沖縄県')], max_length=40, verbose_name='shussin'),
        ),
        migrations.AlterField(
            model_name='user',
            name='tabako',
            field=models.CharField(blank=True, choices=[('suu', '吸う'), ('motomoto', 'もともと吸わない'), ('kinen', '禁煙している')], max_length=40, verbose_name='tabako'),
        ),
    ]
