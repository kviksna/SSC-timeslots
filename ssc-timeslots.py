#@title The code:
import subprocess, json, datetime

#2023-05-01T00:00:00.000Z
def getAPIresponse(strDate):
  cmd = 'curl "https://bookla.com/api/v3/timeslots" -H "Content-Type: application/json" '
  cmd += '-H "SpendoApp: Web/Widget" -H "SpendoDeviceID: e20d129b-e209-4b4a-9aae-1703eb14c224" '
  cmd += '-H "SpendoSig: bf8358a8feeb0ec0124df0506975a3a12636cd29a13de917300e010af4a7f6fe" '
  cmd += '--data-raw \'{"companyId":"042fb9ab-5dd4-4b78-a8ac-d1229322e93d","date":"'
  cmd += strDate
  cmd += '","slotParams":{"serviceId":"09b3b303-fb77-45d9-bcf2-1434b672f679","spots":1,'
  cmd += '"tickets":[{"ticketId":"ecbf6d32-f517-40b1-abc6-3e263ffb2d86","spots":1}]}}\''
  return subprocess.check_output(cmd, shell=True).decode('utf-8').strip()

#{"calendars":[{"calendarId":"e7923fb8-debf-4dc6-9c1e-0eb391a8d0ea","type":"slot","timeslots":[{"startTime":"2023-05-01T11:00:00Z","endTime":"2023-05-01T12:00:00Z","duration":60,"timeZone":"Europe/Riga","price":900,"originalPrice":900,"bankTransferPrice":900,"currency":"eur","slotId":"a760f58b-2053-48e7-9c3b-388fb3aafb0b","spotsTaken":1,"spotsTotal":24,"minSpotsPerUser":1,"maxSpotsPerUser":0,"tickets":[{"id":"01f5f5b0-dbb3-4878-acdd-dd58109855b9","slotId":"a760f58b-2053-48e7-9c3b-388fb3aafb0b","serviceTicketId":"ecbf6d32-f517-40b1-abc6-3e263ffb2d86","title":"","price":900,"originalPrice":900,"currency":"eur"},{"id":"57d2d47e-f079-4b47-9a5d-2942dd5945e6","slotId":"a760f58b-2053-48e7-9c3b-388fb3aafb0b","serviceTicketId":"4576a83a-28a6-4fbc-aad3-1a7584a7c4ff","title":"","price":800,"originalPrice":800,"currency":"eur"},{"id":"c7297976-ee18-480f-bf11-c10432f372f1","slotId":"a760f58b-2053-48e7-9c3b-388fb3aafb0b","serviceTicketId":"8b8bc9ed-baa1-4624-a32b-9838a4c04477","title":"","price":810,"originalPrice":810,"currency":"eur"},{"id":"c99dc398-601e-427e-af61-b5bd01065a84","slotId":"a760f58b-2053-48e7-9c3b-388fb3aafb0b","serviceTicketId":"84ed0ed6-4723-4fb4-811e-a00cf6b1ad7d","title":"","price":720,"originalPrice":720,"currency":"eur"}],"calendarId":"e7923fb8-debf-4dc6-9c1e-0eb391a8d0ea","serviceId":"09b3b303-fb77-45d9-bcf2-1434b672f679","timezone":"Europe/Riga"},{"startTime":"2023-05-01T15:00:00Z","endTime":"2023-05-01T16:00:00Z","duration":60,"timeZone":"Europe/Riga","price":900,"originalPrice":900,"bankTransferPrice":900,"currency":"eur","slotId":"4931bc7f-f11c-4f29-9081-3fde9fb1b552","spotsTaken":1,"spotsTotal":18,"minSpotsPerUser":1,"maxSpotsPerUser":0,"tickets":[{"id":"239de981-7f3f-4cb6-b07d-4722441b8bce","slotId":"4931bc7f-f11c-4f29-9081-3fde9fb1b552","serviceTicketId":"ecbf6d32-f517-40b1-abc6-3e263ffb2d86","title":"","price":900,"originalPrice":900,"currency":"eur"},{"id":"6f80ad64-ace7-4ff8-88a9-dc7e5dec32b2","slotId":"4931bc7f-f11c-4f29-9081-3fde9fb1b552","serviceTicketId":"84ed0ed6-4723-4fb4-811e-a00cf6b1ad7d","title":"","price":720,"originalPrice":720,"currency":"eur"},{"id":"bda9c01b-14c2-42fc-8562-baa110262355","slotId":"4931bc7f-f11c-4f29-9081-3fde9fb1b552","serviceTicketId":"4576a83a-28a6-4fbc-aad3-1a7584a7c4ff","title":"","price":800,"originalPrice":800,"currency":"eur"},{"id":"e274d134-dab1-4002-92d3-543a1e7f2bf0","slotId":"4931bc7f-f11c-4f29-9081-3fde9fb1b552","serviceTicketId":"8b8bc9ed-baa1-4624-a32b-9838a4c04477","title":"","price":810,"originalPrice":810,"currency":"eur"}],"calendarId":"e7923fb8-debf-4dc6-9c1e-0eb391a8d0ea","serviceId":"09b3b303-fb77-45d9-bcf2-1434b672f679","timezone":"Europe/Riga"},{"startTime":"2023-05-01T16:00:00Z","endTime":"2023-05-01T17:00:00Z","duration":60,"timeZone":"Europe/Riga","price":900,"originalPrice":900,"bankTransferPrice":900,"currency":"eur","slotId":"406997b7-7b42-444f-9658-2c534cb09811","spotsTaken":0,"spotsTotal":6,"minSpotsPerUser":1,"maxSpotsPerUser":0,"tickets":[{"id":"33204284-3cd3-4252-836c-4ee294a2861c","slotId":"406997b7-7b42-444f-9658-2c534cb09811","serviceTicketId":"84ed0ed6-4723-4fb4-811e-a00cf6b1ad7d","title":"","price":720,"originalPrice":720,"currency":"eur"},{"id":"5db8e631-7b22-4f44-9aba-e5cdae3e21dd","slotId":"406997b7-7b42-444f-9658-2c534cb09811","serviceTicketId":"4576a83a-28a6-4fbc-aad3-1a7584a7c4ff","title":"","price":800,"originalPrice":800,"currency":"eur"},{"id":"921d9f36-fc4a-43e2-b34a-008b5e7c38bc","slotId":"406997b7-7b42-444f-9658-2c534cb09811","serviceTicketId":"ecbf6d32-f517-40b1-abc6-3e263ffb2d86","title":"","price":900,"originalPrice":900,"currency":"eur"},{"id":"b28b6a2a-57bb-49c5-b8be-cf9f7767d2a1","slotId":"406997b7-7b42-444f-9658-2c534cb09811","serviceTicketId":"8b8bc9ed-baa1-4624-a32b-9838a4c04477","title":"","price":810,"originalPrice":810,"currency":"eur"}],"calendarId":"e7923fb8-debf-4dc6-9c1e-0eb391a8d0ea","serviceId":"09b3b303-fb77-45d9-bcf2-1434b672f679","timezone":"Europe/Riga"}],"shouldHaveTimeSlots":true}]}
def decodeAPIresponse(strData):
  if len(strData)<150:
    #{"calendars":[{"calendarId":"e7923fb8-debf-4dc6-9c1e-0eb391a8d0ea","type":"slot","timeslots":[],"shouldHaveTimeSlots":true}]}
    print(f'{datetime.datetime.now().strftime("%Y.%m.%d")} => EOD')
    return 0
  jData = json.loads(strData)
  utc_timestamp = jData["calendars"][0]["timeslots"][0]["startTime"]
  utc_dt = datetime.datetime.fromisoformat(utc_timestamp.replace('Z', '+00:00'))
  gmt3_timezone = datetime.timezone(datetime.timedelta(hours=3))
  local_dt = utc_dt.astimezone(gmt3_timezone)
  local_timestamp = local_dt.strftime('%Y.%m.%d %H:%M')

  i = 0;
  for elem in jData["calendars"][0]["timeslots"]:
    utc_timestamp = elem["startTime"]
    utc_dt = datetime.datetime.fromisoformat(utc_timestamp.replace('Z', '+00:00'))
    gmt3_timezone = datetime.timezone(datetime.timedelta(hours=3))
    local_dt = utc_dt.astimezone(gmt3_timezone)
    local_timestamp = local_dt.strftime('%Y.%m.%d %H:%M')
    if i == 0:
      print(local_dt.strftime('<br>%Y.%m.%d'), end=" ")
    print(f'{local_dt.strftime("%H:")}({elem["spotsTaken"]}/{elem["spotsTotal"]}) ', end="")
    i += 1
  print("")

def getDaySlots(day):
  now = datetime.datetime.utcnow()
  date = now + datetime.timedelta(days=day)
  date_str = date.strftime("%Y-%m-%dT00:00:00.000Z")
  jStr = getAPIresponse(date_str)
  decodeAPIresponse(jStr)

now = datetime.datetime.now() + datetime.timedelta(hours=3)
print(now.strftime("Now = %Y.%m.%d %H:%M") + " taken/total")
getDaySlots(0)
getDaySlots(1)
getDaySlots(2)
#getDaySlots(3)