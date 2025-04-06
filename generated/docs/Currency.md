# Currency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**enabled** | **bool** | Defaults to true | [optional] [default to True]
**default** | **bool** | Make this currency the native currency. | [optional] 
**native** | **bool** | Make this currency the native currency. | [optional] 
**code** | **str** |  | 
**name** | **str** |  | 
**symbol** | **str** |  | 
**decimal_places** | **int** | Supports 0-16 decimals. | [optional] 

## Example

```python
from openapi_client.models.currency import Currency

# TODO update the JSON string below
json = "{}"
# create an instance of Currency from a JSON string
currency_instance = Currency.from_json(json)
# print the JSON string representation of the object
print(Currency.to_json())

# convert the object into a dict
currency_dict = currency_instance.to_dict()
# create an instance of Currency from a dict
currency_from_dict = Currency.from_dict(currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


