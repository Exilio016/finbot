# RecurrenceTransactionStore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**amount** | **str** | Amount of the transaction. | 
**foreign_amount** | **str** | Foreign amount of the transaction. | [optional] 
**currency_id** | **str** | Submit either a currency_id or a currency_code. | [optional] 
**currency_code** | **str** | Submit either a currency_id or a currency_code. | [optional] 
**foreign_currency_id** | **str** | Submit either a foreign_currency_id or a foreign_currency_code, or neither. | [optional] 
**foreign_currency_code** | **str** | Submit either a foreign_currency_id or a foreign_currency_code, or neither. | [optional] 
**budget_id** | **str** | The budget ID for this transaction. | [optional] 
**category_id** | **str** | Category ID for this transaction. | [optional] 
**source_id** | **str** | ID of the source account. | 
**destination_id** | **str** | ID of the destination account. | 
**tags** | **List[str]** | Array of tags. | [optional] 
**piggy_bank_id** | **str** | Optional. | [optional] 
**bill_id** | **str** | Optional. | [optional] 

## Example

```python
from openapi_client.models.recurrence_transaction_store import RecurrenceTransactionStore

# TODO update the JSON string below
json = "{}"
# create an instance of RecurrenceTransactionStore from a JSON string
recurrence_transaction_store_instance = RecurrenceTransactionStore.from_json(json)
# print the JSON string representation of the object
print(RecurrenceTransactionStore.to_json())

# convert the object into a dict
recurrence_transaction_store_dict = recurrence_transaction_store_instance.to_dict()
# create an instance of RecurrenceTransactionStore from a dict
recurrence_transaction_store_from_dict = RecurrenceTransactionStore.from_dict(recurrence_transaction_store_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


