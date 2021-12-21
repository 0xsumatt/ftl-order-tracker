import requests
import json
import csv
from discord_webhook import DiscordWebhook, DiscordEmbed
from urllib.parse import urljoin
import random

print('What would you like to track ?')
print('1.FTL - Ganesh')
print('2.FTL - Other bots')
choice = input('>')
if choice == '1':
    try:

        def get_tracking():

            with open('successful_checkouts.csv', 'r') as csvFile:
                csv_reader = csv.DictReader(csvFile)

                for row in csv_reader:
                    with open('proxies.txt', 'r') as proxies_in:
                        proxy_lines = proxies_in.read().splitlines()

                    proxyList = [i for i in proxy_lines]
                    proxies_use = random.choice(proxyList)
                    proxies_use = proxies_use.split(':')

                    try:
                        proxies = {

                            'http': f'http://{proxies_use[2]}:{proxies_use[3]}@{proxies_use[0]}:{proxies_use[1]}',
                            'https': f'https://{proxies_use[2]}:{proxies_use[3]}@{proxies_use[0]}:{proxies_use[1]}'
                        }
                    except:

                        proxies = {
                            'http': f'http://{proxies_use[0]}:{proxies_use[1]}',
                            'https': f'https://{proxies_use[0]}:{proxies_use[1]}',


                        }

                    Order_number = row['Order Number']
                    print(Order_number)
                    Date = row['Date Time']
                    email_used = row['Email']
                    size = row['Size']
                    s = requests.session()
                    base_url = 'https://footlocker.narvar.com/tracking/itemvisibility/v1/footlocker/orders/{}'.format(
                        Order_number)
                    print(base_url)
                    email_used = row['Email']
                    track = s.get(base_url, proxies=proxies)

                    if track.status_code == 200:

                        status_dict = json.loads(track.text)

                        Item_name = (status_dict['order_info']
                                     ['order_items'][0]['name'])
                        Item_image = (status_dict['order_info']
                                      ['order_items'][0]['item_image'])
                        image_url = urljoin('https:', Item_image)

                        order_status = (status_dict['order_info']
                                        ['order_items'][0]['fulfillment_status'])

                        if order_status == 'SHIPPED':
                            ship_date = (status_dict['order_info']
                                         ['shipments'][0]['ship_date'])

                        webhook_url = open('webhook.txt', 'r')
                        hook = DiscordWebhook(webhook_url.readline())

                        embed = DiscordEmbed(
                            title=Item_name, url=base_url, color=0xA8E6CE)
                        embed.set_thumbnail(url=image_url)
                        embed.add_embed_field(name='Order Number',
                                              value='||'+Order_number+'||')
                        embed.add_embed_field(name='Size', value=size)
                        embed.add_embed_field(name='Order Date', value=Date,)
                        embed.add_embed_field(name='Order Status',
                                              value=order_status, inline=True)
                        embed.add_embed_field(
                            name='Email', value='||'+email_used + '||')
                        if order_status == 'SHIPPED':
                            embed.add_embed_field(name='Ship Date',
                                                  value=ship_date, inline=True)

                        embed.set_footer(icon_url='https://i.imgur.com/VpbdoDn.jpg',
                                         text='  By Sumatt#0001|  ')
                        response = hook.execute()

        get_tracking()
    except IndexError:
        with open('successful_checkouts.csv', 'r') as csvFile:
            csv_reader = csv.DictReader(csvFile)

            for row in csv_reader:
                with open('proxies.txt', 'r') as proxies_in:
                    proxy_lines = proxies_in.read().splitlines()

                proxyList = [i for i in proxy_lines]
                proxies_use = random.choice(proxyList)
                proxies_use = proxies_use.split(':')

                try:
                    proxies = {

                        'http': f'http://{proxies_use[2]}:{proxies_use[3]}@{proxies_use[0]}:{proxies_use[1]}',
                        'https': f'https://{proxies_use[2]}:{proxies_use[3]}@{proxies_use[0]}:{proxies_use[1]}'
                    }
                except:

                    proxies = {
                        'http': f'http://{proxies_use[0]}:{proxies_use[1]}',
                        'https': f'https://{proxies_use[0]}:{proxies_use[1]}'
                    }

                Order_number = row['Order Number']
                print(Order_number)
                Date = row['Date Time']
                email_used = row['Email']
                size = row['Size']
                s = requests.session()
                base_url = 'https://footlocker.narvar.com/tracking/itemvisibility/v1/footlocker/orders/{}'.format(
                    Order_number)
                print(base_url)
                email_used = row['Email']
                track = s.get(base_url)

                if track.status_code == 200:

                    status_dict = json.loads(track.text)

                    webhook_url = open('webhook.txt', 'r')
                    hook = DiscordWebhook(webhook_url.readline())

                    embed = DiscordEmbed(title='Order Info', url=base_url)
                    embed.set_thumbnail(
                        url='https://assets.change.org/photos/1/xa/nx/VUXaNxSqVncKCum-800x450-noPad.jpg?1537026680')

                    embed.add_embed_field(name='Order Number',
                                          value='||'+Order_number+'||')
                    embed.add_embed_field(
                        name='Email', value='||'+email_used+'||')
                    embed.add_embed_field(
                        name='Status', value='Your order has probably been cancelled')
                    embed.set_footer(icon_url='https://i.imgur.com/VpbdoDn.jpg',
                                     text='  By Sumatt#0001|  ')
                    response = hook.execute()


if choice == '2':

    try:

        def otherbots():
            with open('orders.csv', 'r') as csvFile:
                csv_reader = csv.DictReader(csvFile)

                for row in csv_reader:
                    with open('proxies.txt', 'r') as proxies_in:
                        proxy_lines = proxies_in.read().splitlines()

                    proxyList = [i for i in proxy_lines]
                    proxies_use = random.choice(proxyList)
                    proxies_use = proxies_use.split(':')

                    try:
                        proxies = {

                            'http': f'http://{proxies_use[2]}:{proxies_use[3]}@{proxies_use[0]}:{proxies_use[1]}',
                            'https': f'https://{proxies_use[2]}:{proxies_use[3]}@{proxies_use[0]}:{proxies_use[1]}'
                        }
                    except:

                        proxies = {
                            'http': f'http://{proxies_use[0]}:{proxies_use[1]}',
                            'https': f'https://{proxies_use[0]}:{proxies_use[1]}'
                        }

                    Order_number = row['Order Number']

                    email_use = row['Email']
                    s = requests.session()
                    base_url = 'https://footlocker.narvar.com/tracking/itemvisibility/v1/footlocker/orders/{}'.format(
                        Order_number)

                    tracker = s.get(base_url, proxies=proxies)
                    if tracker.status_code == 200:
                        status_dict = json.loads(tracker.text)
                        Item_name = (status_dict['order_info']
                                     ['order_items'][0]['name'])
                        Item_Sku = (status_dict['order_info']
                                    ['order_items'][0]['sku'])
                        Item_image = (status_dict['order_info']
                                      ['order_items'][0]['item_image'])
                        image_url = urljoin('https:', Item_image)

                        order_status = (status_dict['order_info']
                                        ['order_items'][0]['fulfillment_status'])

                        if order_status == 'SHIPPED':
                            ship_date = (status_dict['order_info']
                                         ['shipments'][0]['ship_date'])

                        webhook_url = open('webhook.txt', 'r')
                        hook = DiscordWebhook(webhook_url.readline())

                        embed = Embed()

                        embed.color = 0xA8E6CE
                        embed.set_title(title=Item_name, url=base_url)
                        embed.set_thumbnail(url=image_url)
                        embed.add_field(name='Order Number',
                                        value='||'+Order_number+'||')

                        embed.add_field(name='Order SKU',
                                        value=Item_Sku)

                        embed.add_field(name='Order Status',
                                        value=order_status, inline=True)
                        embed.add_field(
                            name='Email', value='||'+email_use + '||')
                        if order_status == 'SHIPPED':
                            embed.add_field(name='Ship Date',
                                            value=ship_date, inline=True)

                        embed.set_footer(icon_url='https://i.imgur.com/VpbdoDn.jpg',
                                         text='  By Sumatt#0001|  ')
                        hook.send(embed=embed)

        otherbots()

    except IndexError:
        with open('successful_checkouts.csv', 'r') as csvFile:
            csv_reader = csv.DictReader(csvFile)

            for row in csv_reader:
                with open('proxies.txt', 'r') as proxies_in:
                    proxy_lines = proxies_in.read().splitlines()

                proxyList = [i for i in proxy_lines]
                proxies_use = random.choice(proxyList)
                proxies_use = proxies_use.split(':')

                try:
                    proxies = {

                        'http': f'http://{proxies_use[2]}:{proxies_use[3]}@{proxies_use[0]}:{proxies_use[1]}',
                        'https': f'https://{proxies_use[2]}:{proxies_use[3]}@{proxies_use[0]}:{proxies_use[1]}'
                    }
                except:

                    proxies = {
                        'http': f'http://{proxies_use[0]}:{proxies_use[1]}',
                        'https': f'https://{proxies_use[0]}:{proxies_use[1]}'
                    }
                Order_number = row['Order Number']

                email_use = row['Email']
                s = requests.session()
                base_url = 'https://footlocker.narvar.com/tracking/itemvisibility/v1/footlocker/orders/{}'.format(
                    Order_number)
                print(base_url)
                tracker = s.get(base_url, proxies=proxies)
                if tracker.status_code == 200:
                    status_dict = json.loads(track.text)

                    webhook_url = open('webhook.txt', 'r')
                    hook = Webhook(webhook_url.readline())

                    embed = Embed()
                    embed.color = 0xA62639
                    embed.set_title(title='Order Info', url=base_url)
                    embed.set_thumbnail(
                        url='https://assets.change.org/photos/1/xa/nx/VUXaNxSqVncKCum-800x450-noPad.jpg?1537026680')

                    embed.add_field(name='Order Number',
                                    value='||'+Order_number+'||')
                    embed.add_field(
                        name='Email', value='||'+email_used+'||')
                    embed.add_field(
                        name='Status', value='Your order has probably been cancelled')
                    embed.set_footer(
                        icon_url='https://i.imgur.com/VpbdoDn.jpg', text='  By Sumatt#0001|  ')
                    hook.send(embed=embed)


if choice == '3':
    def disney():
        print('enter your email')
        email = input('>')
        print('enter your order number')
        Disney_order = input('')
    disney()
