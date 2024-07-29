##
# DEPENDENCIES
# Warning: these are extracted from your function files, if you need to make changes edit the function file and recompile this task.
##

import requests
    
##
# LIBRARY FUNCTIONS
# Warning: these are common functions, if you need to make changes edit the function file and recompile this task.
##

def preserve_order(ids, data, key):
    """
    Preserves the order of items based on the list of IDs.

    Args:
        ids (list): The list of IDs.
        data (list): The list of data dictionaries.
        key (str): The key to match IDs in data.

    Returns:
        list: A list of data dictionaries in the order of the given IDs.
    """
    data_dict = {item[key]: item for item in data}
    return [data_dict[id] for id in ids if id in data_dict]


##
# PUBLIC FUNCTIONS
# Warning: these are common functions, if you need to make changes edit the function file and recompile this task.
##

def get_banks_by_name(name):
    """
    Fetches a list of banks by name.

    Args:
        name (str): The name of the bank.

    Returns:
        list: A list of dictionaries containing bank ID and name.
    """
    url = f"https://banks.data.fdic.gov/api/institutions?filters=ACTIVE%3A1&search=NAME:{requests.utils.quote(name)}&fields=NAME&limit=10000"
    response = requests.get(url)
    data = response.json().get('data', [])
    return [item['data'] for item in data]



def get_banks_by_list_of_states(state_codes):
    """
    Fetches a list of banks by state codes.

    Args:
        state_codes (list of str): A list of state codes.

    Returns:
        list: A list of dictionaries containing bank ID and name.
    """
    states_filter = " OR ".join([f"STALP:{requests.utils.quote(state)}" for state in state_codes])
    url = f"https://banks.data.fdic.gov/api/institutions?filters=ACTIVE%3A1 AND {states_filter}&fields=ID,NAME&limit=10000"
    response = requests.get(url)
    data = response.json().get('data', [])
    return [item['data'] for item in data]



def get_top_n_banks_from_list(bank_ids, sort_by, sort_order, limit):
    """
    Fetches the top N banks from a list of bank IDs.

    Args:
        bank_ids (list of int): A list of bank IDs.
        sort_by (str): The field to sort by. Possible values are ASSET, NETINC, DEP, DEPDOM, ROE, ROA, DATEUPDT, OFFICES, OFFDOM, OFFFOR, OFFOA.
        sort_order (str): The order to sort by. Possible values are ASC, DESC.
        limit (int): The maximum number of banks to return.

    Returns:
        list: A list of dictionaries containing bank ID and name.
    """
    ids_filter = " OR ".join([f"CERT:{bank_id}" for bank_id in bank_ids])
    url = f"https://banks.data.fdic.gov/api/institutions?filters={ids_filter}&fields=ID,NAME&limit={limit}&sort_by={sort_by}&sort_order={sort_order}"
    response = requests.get(url)
    data = response.json().get('data', [])
    return [item['data'] for item in data]



def get_top_n_banks(sort_by, sort_order, limit):
    """
    Fetches the top N banks.

    Args:
        sort_by (str): The field to sort by. Possible values are ASSET, NETINC, DEP, DEPDOM, ROE, ROA, DATEUPDT, OFFICES, OFFDOM, OFFFOR, OFFOA.
        sort_order (str): The order to sort by. Possible values are ASC, DESC.
        limit (int): The maximum number of banks to return.

    Returns:
        list: A list of dictionaries containing bank ID and name.
    """
    url = f"https://banks.data.fdic.gov/api/institutions?fields=ID,NAME&limit={limit}&sort_by={sort_by}&sort_order={sort_order}"
    response = requests.get(url)
    data = response.json().get('data', [])
    return [item['data'] for item in data]



def get_general_and_financial_bank_info_from_list(bank_ids):
    """
    Fetches general and financial information of banks from a list of bank IDs.

    Args:
        bank_ids (list of int): A list of bank IDs.

    Returns:
        list: A list of dictionaries containing bank information with fields:
              ACTIVE, ADDRESS, ADDRESS2, CITY, COUNTY, NAME, PRIORNAME1, PRIORNAME2, 
              PRIORNAME3, PRIORNAME4, PRIORNAME5, PRIORNAME6, PRIORNAME7, PRIORNAME8, 
              PRIORNAME9, PRIORNAME10, STALP, STNAME, ZIP, WEBADDR, OFFICES, ASSET, 
              DEP, DEPDOM, NETINC, NETINCQ, EQ, ROA, ROAPTX, ROAPTXQ, ROAQ, ROE, ROEQ.
    """
    ids_filter = " OR ".join([f"CERT:{bank_id}" for bank_id in bank_ids])
    url = f"https://banks.data.fdic.gov/api/institutions?filters={ids_filter}&fields=ACTIVE,ADDRESS,ADDRESS2,CITY,COUNTY,NAME,PRIORNAME1,PRIORNAME2,PRIORNAME3,PRIORNAME4,PRIORNAME5,PRIORNAME6,PRIORNAME7,PRIORNAME8,PRIORNAME9,PRIORNAME10,STALP,STNAME,ZIP,WEBADDR,OFFICES,ASSET,DEP,DEPDOM,NETINC,NETINCQ,EQ,ROA,ROAPTX,ROAPTXQ,ROAQ,ROE,ROEQ&limit=1000"
    response = requests.get(url)
    data = response.json().get('data', [])
    return preserve_order(bank_ids, [item['data'] for item in data], 'ID')



def get_location_and_geographical_bank_info_from_list(bank_ids):
    """
    Fetches location and geographical information of banks from a list of bank IDs.

    Args:
        bank_ids (list of int): A list of bank IDs.

    Returns:
        list: A list of dictionaries containing bank information with fields:
              ID, CBSA, CBSA_DIV, CBSA_DIV_FLG, CBSA_DIV_NO, CBSA_METRO, CBSA_METRO_FLG, 
              CBSA_METRO_NAME, CBSA_MICRO_FLG, CBSA_NO, CMSA, CMSA_NO, CSA, CSA_FLG, CSA_NO, 
              MSA, MSA_NO, CITYHCR, STALPHCR, STCHRTR, STCNTY, TRACT, LATITUDE, LONGITUDE.
    """
    ids_filter = " OR ".join([f"CERT:{bank_id}" for bank_id in bank_ids])
    url = f"https://banks.data.fdic.gov/api/institutions?filters={ids_filter}&fields=ID,CBSA,CBSA_DIV,CBSA_DIV_FLG,CBSA_DIV_NO,CBSA_METRO,CBSA_METRO_FLG,CBSA_METRO_NAME,CBSA_MICRO_FLG,CBSA_NO,CMSA,CMSA_NO,CSA,CSA_FLG,CSA_NO,MSA,MSA_NO,CITYHCR,STALPHCR,STCHRTR,STCNTY,TRACT,LATITUDE,LONGITUDE&limit=1000"
    response = requests.get(url)
    data = response.json().get('data', [])
    return preserve_order(bank_ids, [item['data'] for item in data], 'ID')



def get_regulatory_bank_info_from_list(bank_ids):
    """
    Fetches regulatory information of banks from a list of bank IDs.

    Args:
        bank_ids (list of int): A list of bank IDs.

    Returns:
        list: A list of dictionaries containing bank information with fields:
              ID, BKCLASS, CHRTAGNT, CFPBFLAG, CONSERVE, DENOVO, FDICDBS, FDICREGN, 
              FDICSUPV, FED, FED_RSSD, FEDCHRTR, FLDOFF, FORM31, HCTMULT, INSAGNT1, 
              INSAGNT2, INSBIF, INSCOML, INSDATE, INSDIF, INSDROPDATE, INSDROPDATE_RAW, 
              INSFDIC, INSSAIF, INSSAVE, INSTAG, INSTCRCD, LAW_SASSER_FLG, MDI_STATUS_CODE, 
              MDI_STATUS_DESC, MUTUAL, OAKAR, OCCDIST, OTSDIST, OTSREGNM, REGAGNT, REGAGENT2, 
              SPECGRP, SPECGRPN, SUBCHAPS, SUPRV_FD, SASSER, TRUST.
    """
    ids_filter = " OR ".join([f"CERT:{bank_id}" for bank_id in bank_ids])
    url = f"https://banks.data.fdic.gov/api/institutions?filters={ids_filter}&fields=ID,BKCLASS,CHRTAGNT,CFPBFLAG,CONSERVE,DENOVO,FDICDBS,FDICREGN,FDICSUPV,FED,FED_RSSD,FEDCHRTR,FLDOFF,FORM31,HCTMULT,INSAGNT1,INSAGNT2,INSBIF,INSCOML,INSDATE,INSDIF,INSDROPDATE,INSDROPDATE_RAW,INSFDIC,INSSAIF,INSSAVE,INSTAG,INSTCRCD,LAW_SASSER_FLG,MDI_STATUS_CODE,MDI_STATUS_DESC,MUTUAL,OAKAR,OCCDIST,OTSDIST,OTSREGNM,REGAGNT,REGAGENT2,SPECGRP,SPECGRPN,SUBCHAPS,SUPRV_FD,SASSER,TRUST&limit=1000"
    response = requests.get(url)
    data = response.json().get('data', [])
    return preserve_order(bank_ids, [item['data'] for item in data], 'ID')



def get_bank_branches(bank_ids):
    """
    Fetches branches information of banks from a list of bank IDs.

    Args:
        bank_ids (list of int): A list of bank IDs.

    Returns:
        list: A list of dictionaries containing bank branch information with fields:
              ADDRESS, BKCLASS, CBSA, CBSA_DIV, CBSA_DIV_FLG, CBSA_DIV_NO, CBSA_METRO, 
              CBSA_METRO_FLG, CBSA_METRO_NAME, CBSA_MICRO_FLG, CBSA_NO, CERT, CITY, COUNTY, 
              CSA, CSA_FLG, CSA_NO, ESTYMD, FI_UNINUM, LATITUDE, LONGITUDE, MDI_STATUS_CODE, 
              MDI_STATUS_DESC, MAINOFF, NAME, OFFNAME, OFFNUM, RUNDATE, SERVTYPE, SERVTYPE_DESC, 
              STALP, STCNTY, STNAME, UNINUM, ZIP.
    """
    ids_filter = " OR ".join([f"CERT:{bank_id}" for bank_id in bank_ids])
    url = f"https://banks.data.fdic.gov/api/locations?filters={ids_filter}&fields=ADDRESS,BKCLASS,CBSA,CBSA_DIV,CBSA_DIV_FLG,CBSA_DIV_NO,CBSA_METRO,CBSA_METRO_FLG,CBSA_METRO_NAME,CBSA_MICRO_FLG,CBSA_NO,CERT,CITY,COUNTY,CSA,CSA_FLG,CSA_NO,ESTYMD,FI_UNINUM,LATITUDE,LONGITUDE,MDI_STATUS_CODE,MDI_STATUS_DESC,MAINOFF,NAME,OFFNAME,OFFNUM,RUNDATE,SERVTYPE,SERVTYPE_DESC,STALP,STCNTY,STNAME,UNINUM,ZIP&sort_by=NAME&sort_order=DESC&limit=10000"
    response = requests.get(url)
    data = response.json().get('data', [])
    return [item['data'] for item in data]



def get_banks_with_branches_in_list_of_states(state_codes):
    """
    Fetches banks with branches in a list of state codes.

    Args:
        state_codes (list of str): A list of state codes.

    Returns:
        list: A list of dictionaries containing bank ID and name.
    """
    states_filter = " OR ".join([f"STALP:{state}" for state in state_codes])
    url = f"https://banks.data.fdic.gov/api/locations?filters={states_filter}&fields=CERT,STALP&limit=10000"
    response = requests.get(url)
    data = response.json().get('data', [])
    results_with_duplicates = [{'ID': item['data']['CERT'], 'NAME': item['data']['NAME']} for item in data]
    unique_results = {item['ID']: item for item in results_with_duplicates}
    return list(unique_results.values())



##
# GENERATED CODE
# This function is the generated code: it's safe to edit.
##

def doTask(bank_ids: str):
    import json
    bank_id_list = [int(bank_id) for bank_id in bank_ids.split('|')]
    regulatory_info = get_regulatory_bank_info_from_list(bank_id_list)
    print(json.dumps(regulatory_info))
