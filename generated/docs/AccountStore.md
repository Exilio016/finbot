# AccountStore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | [**ShortAccountTypeProperty**](ShortAccountTypeProperty.md) |  | 
**iban** | **str** |  | [optional] 
**bic** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**opening_balance** | **str** | Represents the opening balance, the initial amount this account holds. | [optional] 
**opening_balance_date** | **datetime** | Represents the date of the opening balance. | [optional] 
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
**liability_direction** | [**LiabilityDirectionProperty**](LiabilityDirectionProperty.md) |  | [optional] 
**interest** | **str** | Mandatory when type is liability. Interest percentage. | [optional] [default to '0']
**interest_period** | [**InterestPeriodProperty**](InterestPeriodProperty.md) |  | [optional] 
**notes** | **str** |  | [optional] 
**latitude** | **float** | Latitude of the accounts&#39;s location, if applicable. Can be used to draw a map. | [optional] 
**longitude** | **float** | Latitude of the accounts&#39;s location, if applicable. Can be used to draw a map. | [optional] 
**zoom_level** | **int** | Zoom level for the map, if drawn. This to set the box right. Unfortunately this is a proprietary value because each map provider has different zoom levels. | [optional] 

## Example

```python
from openapi_client.models.account_store import AccountStore

# TODO update the JSON string below
json = "{}"
# create an instance of AccountStore from a JSON string
account_store_instance = AccountStore.from_json(json)
# print the JSON string representation of the object
print(AccountStore.to_json())

# convert the object into a dict
account_store_dict = account_store_instance.to_dict()
# create an instance of AccountStore from a dict
account_store_from_dict = AccountStore.from_dict(account_store_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


