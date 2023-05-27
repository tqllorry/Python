def transform(dict):
    referrer = dict["referrer"]

    if 'ref' in dict.keys():
        dict["ref"] = referrer if len(dict["ref"]) == 0 else dict["ref"]
    else:
        dict["ref"] = referrer

    return dict


aaa = {
  "referrer": "https://km.lexiangla.net/exams/004d67907e7b11ec8537c68463c07c1b/manage?map=2147&company_from=km",
  "ref": ""
 }

bbb = transform(aaa)

print(bbb)