import pandas

madataframe = pandas.read_csv("export-operations.csv", encoding="cp1252", delimiter=";")
madataframe["payment"] = ""
madataframe.loc[madataframe["label"].str.contains("VIR"), ["payment"]] = 4
madataframe.loc[madataframe["label"].str.contains("CB"), ["payment"]] = 1
madataframe.loc[madataframe["label"].str.contains("CARTE"), ["payment"]] = 1
madataframe.loc[madataframe["label"].str.contains("PRLV SEPA"), ["payment"]] = 10
madataframe["info"] = madataframe["label"]
madataframe = madataframe.drop(columns="dateVal")
madataframe = madataframe.drop(columns="categoryParent")
madataframe = madataframe.drop(columns="accountbalance")
madataframe = madataframe.drop(columns="accountNum")
madataframe = madataframe.drop(columns="accountLabel")
madataframe = madataframe.rename(columns={"dateOp": "date"})
madataframe["memo"] = ""
madataframe["tags"] = ""
madataframe["payee"] = ""

madataframe = madataframe[["date", "payment", "info", "payee", "memo", "amount", "category", "tags"]]

madataframe.to_csv("output.csv", index=False, quoting=None, sep=";")