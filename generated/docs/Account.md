# Account


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**active** | **bool** | If omitted, defaults to true. | [optional] [default to True]
**order** | **int** | Order of the account. Is NULL if account is not asset or liability. | [optional] 
**name** | **str** |  | 
**type** | [**ShortAccountTypeProperty**](ShortAccountTypeProperty.md) |  | 
**account_role** | [**AccountRoleProperty**](AccountRoleProperty.md) |  | [optional] 
**currency_id** | **str** | Use either currency_id or currency_code. Defaults to the user&#39;s default currency. | [optional] 
**currency_code** | **str** | Use either currency_id or currency_code. Defaults to the user&#39;s default currency. | [optional] 
**currency_symbol** | **str** |  | [optional] [readonly] 
**currency_decimal_places** | **int** |  | [optional] [readonly] 
**native_currency_id** | **str** | Returns the native currency ID of the administration. | [optional] [readonly] 
**native_currency_code** | **str** | Returns the native currency code of the administration. | [optional] 
**native_currency_symbol** | **str** | Returns the native currency symbol of the administration. | [optional] [readonly] 
**native_currency_decimal_places** | **int** | Returns the native currency decimal places of the administration. | [optional] [readonly] 
**current_balance** | **str** | The current balance of the account in the account&#39;s currency OR the native currency if the account has no currency. | [optional] [readonly] 
**native_current_balance** | **str** | The current balance of the account in the administration&#39;s native currency. | [optional] [readonly] 
**current_balance_date** | **datetime** | The timestamp for this date is always 23:59:59, to indicate it&#39;s the balance at the very END of that particular day. | [optional] [readonly] 
**notes** | **str** |  | [optional] 
**monthly_payment_date** | **datetime** | Mandatory when the account_role is ccAsset. Moment at which CC payment installments are asked for by the bank. | [optional] 
**credit_card_type** | [**CreditCardTypeProperty**](CreditCardTypeProperty.md) |  | [optional] 
**account_number** | **str** |  | [optional] 
**iban** | **str** |  | [optional] 
**bic** | **str** |  | [optional] 
**virtual_balance** | **str** | The virtual balance of the account in the account&#39;s currency or the administration&#39;s native currency if the account has no currency. | [optional] 
**native_virtual_balance** | **str** | The virtual balance of the account in administration&#39;s native currency. | [optional] 
**opening_balance** | **str** | Represents the opening balance, the initial amount this account holds in the currency of the account or the administration&#39;s native currency if the account has no currency. | [optional] 
**native_opening_balance** | **str** | Represents the opening balance, in the administration&#39;s native currency. | [optional] 
**opening_balance_date** | **datetime** | Represents the date of the opening balance. | [optional] 
**liability_type** | [**LiabilityTypeProperty**](LiabilityTypeProperty.md) |  | [optional] 
**liability_direction** | [**LiabilityDirectionProperty**](LiabilityDirectionProperty.md) |  | [optional] 
**interest** | **str** | Mandatory when type is liability. Interest percentage. | [optional] 
**interest_period** | [**InterestPeriodProperty**](InterestPeriodProperty.md) |  | [optional] 
**current_debt** | **str** | Represents the current debt for liabilities. | [optional] 
**include_net_worth** | **bool** | If omitted, defaults to true. | [optional] [default to True]
**longitude** | **float** | Latitude of the accounts&#39;s location, if applicable. Can be used to draw a map. | [optional] 
**latitude** | **float** | Latitude of the accounts&#39;s location, if applicable. Can be used to draw a map. | [optional] 
**zoom_level** | **int** | Zoom level for the map, if drawn. This to set the box right. Unfortunately this is a proprietary value because each map provider has different zoom levels. | [optional] 

## Example

```python
from openapi_client.models.account import Account

# TODO update the JSON string below
json = "{}"
# create an instance of Account from a JSON string
account_instance = Account.from_json(json)
# print the JSON string representation of the object
print(Account.to_json())

# convert the object into a dict
account_dict = account_instance.to_dict()
# create an instance of Account from a dict
account_from_dict = Account.from_dict(account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


