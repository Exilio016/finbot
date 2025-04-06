# AccountUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**iban** | **str** |  | [optional] 
**bic** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**opening_balance** | **str** |  | [optional] 
**opening_balance_date** | **datetime** |  | [optional] 
**virtual_balance** | **str** |  | [optional] 
**currency_id** | **str** | Use either currency_id or currency_code. Defaults to the user&#39;s default currency. | [optional] 
**currency_code** | **str** | Use either currency_id or currency_code. Defaults to the user&#39;s default currency. | [optional] 
**active** | **bool** | If omitted, defaults to true. | [optional] [default to True]
**order** | **int** | Order of the account | [optional] 
**include_net_worth** | **bool** | If omitted, defaults to true. | [optional] [default to True]
**account_role** | [**AccountRoleProperty**](AccountRoleProperty.md) |  | [optional] 
**credit_card_type** | [**CreditCardTypeProperty**](CreditCardTypeProperty.md) |  | [optional] 
**monthly_payment_date** | **datetime** | Mandatory when the account_role is ccAsset. Moment at which CC payment installments are asked for by the bank. | [optional] 
**liability_type** | [**LiabilityTypeProperty**](LiabilityTypeProperty.md) |  | [optional] 
**interest** | **str** | Mandatory when type is liability. Interest percentage. | [optional] 
**interest_period** | [**InterestPeriodProperty**](InterestPeriodProperty.md) |  | [optional] 
**notes** | **str** |  | [optional] 
**latitude** | **float** | Latitude of the account&#39;s location, if applicable. Can be used to draw a map. If omitted, the existing location will be kept. If submitted as NULL, the current location will be removed. | [optional] 
**longitude** | **float** | Latitude of the account&#39;s location, if applicable. Can be used to draw a map. If omitted, the existing location will be kept. If submitted as NULL, the current location will be removed. | [optional] 
**zoom_level** | **int** | Zoom level for the map, if drawn. This to set the box right. Unfortunately this is a proprietary value because each map provider has different zoom levels. If omitted, the existing location will be kept. If submitted as NULL, the current location will be removed. | [optional] 

## Example

```python
from openapi_client.models.account_update import AccountUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AccountUpdate from a JSON string
account_update_instance = AccountUpdate.from_json(json)
# print the JSON string representation of the object
print(AccountUpdate.to_json())

# convert the object into a dict
account_update_dict = account_update_instance.to_dict()
# create an instance of AccountUpdate from a dict
account_update_from_dict = AccountUpdate.from_dict(account_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


