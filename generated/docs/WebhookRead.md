# WebhookRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Immutable value | 
**id** | **str** |  | 
**attributes** | [**Webhook**](Webhook.md) |  | 
**links** | [**ObjectLink**](ObjectLink.md) |  | 

## Example

```python
from openapi_client.models.webhook_read import WebhookRead

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRead from a JSON string
webhook_read_instance = WebhookRead.from_json(json)
# print the JSON string representation of the object
print(WebhookRead.to_json())

# convert the object into a dict
webhook_read_dict = webhook_read_instance.to_dict()
# create an instance of WebhookRead from a dict
webhook_read_from_dict = WebhookRead.from_dict(webhook_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


