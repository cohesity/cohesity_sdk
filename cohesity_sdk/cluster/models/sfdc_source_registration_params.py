# coding: utf-8

"""
    Cohesity REST API

    Cohesity API provides a RESTful interface to access the various data management operations on Cohesity cluster and Helios.

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Set
from typing_extensions import Self

class SfdcSourceRegistrationParams(BaseModel):
    """
    Specifies parameters to register an SFDC Protection Source.
    """ # noqa: E501
    auth_token: Optional[StrictStr] = Field(description="Specifies the token that will be used for fetching oAuth tokens from salesforce.", alias="authToken")
    callback_url: Optional[StrictStr] = Field(default=None, description="Specifies the URL added in the connected apps Callback URL field. You can find this URL on the connected apps Manage Connected Apps page or from the connected apps definition. This value must be URL encoded.", alias="callbackUrl")
    concurrent_api_requests_limit: Optional[StrictInt] = Field(description="Specifies the maximum number of concurrent API requests allowed for salesforce.", alias="concurrentApiRequestsLimit")
    consumer_key: Optional[StrictStr] = Field(description="Specifies Consumer key from the connected app in SFDC.", alias="consumerKey")
    consumer_secret: Optional[StrictStr] = Field(description="Specifies Consumer secret from the connected app in SFDC.", alias="consumerSecret")
    daily_api_limit: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(description="Specifies the maximum number of daily API requests allowed for salesforce.", alias="dailyApiLimit")
    endpoint: Optional[StrictStr] = Field(description="Specifies the SFDC endpoint URL.")
    endpoint_type: Optional[StrictStr] = Field(description="SFDC Endpoint type.", alias="endpointType")
    metadata_endpoint_url: Optional[StrictStr] = Field(default=None, description="Specifies the url to access salesforce metadata requests.", alias="metadataEndpointUrl")
    password: Optional[StrictStr] = Field(default=None, description="Specifies the password to access salesforce.")
    soap_endpoint_url: Optional[StrictStr] = Field(default=None, description="Specifies the url to access salesforce soap requests.", alias="soapEndpointUrl")
    username: Optional[StrictStr] = Field(default=None, description="Specifies the username to access salesforce.")
    __properties: ClassVar[List[str]] = ["authToken", "callbackUrl", "concurrentApiRequestsLimit", "consumerKey", "consumerSecret", "dailyApiLimit", "endpoint", "endpointType", "metadataEndpointUrl", "password", "soapEndpointUrl", "username"]

    @field_validator('endpoint_type')
    def endpoint_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['PROD', 'SANDBOX', 'OTHER']):
            raise ValueError("must be one of enum values ('PROD', 'SANDBOX', 'OTHER')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SfdcSourceRegistrationParams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "metadata_endpoint_url",
            "soap_endpoint_url",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if auth_token (nullable) is None
        # and model_fields_set contains the field
        if self.auth_token is None and "auth_token" in self.model_fields_set:
            _dict['authToken'] = None

        # set to None if callback_url (nullable) is None
        # and model_fields_set contains the field
        if self.callback_url is None and "callback_url" in self.model_fields_set:
            _dict['callbackUrl'] = None

        # set to None if concurrent_api_requests_limit (nullable) is None
        # and model_fields_set contains the field
        if self.concurrent_api_requests_limit is None and "concurrent_api_requests_limit" in self.model_fields_set:
            _dict['concurrentApiRequestsLimit'] = None

        # set to None if consumer_key (nullable) is None
        # and model_fields_set contains the field
        if self.consumer_key is None and "consumer_key" in self.model_fields_set:
            _dict['consumerKey'] = None

        # set to None if consumer_secret (nullable) is None
        # and model_fields_set contains the field
        if self.consumer_secret is None and "consumer_secret" in self.model_fields_set:
            _dict['consumerSecret'] = None

        # set to None if daily_api_limit (nullable) is None
        # and model_fields_set contains the field
        if self.daily_api_limit is None and "daily_api_limit" in self.model_fields_set:
            _dict['dailyApiLimit'] = None

        # set to None if endpoint (nullable) is None
        # and model_fields_set contains the field
        if self.endpoint is None and "endpoint" in self.model_fields_set:
            _dict['endpoint'] = None

        # set to None if endpoint_type (nullable) is None
        # and model_fields_set contains the field
        if self.endpoint_type is None and "endpoint_type" in self.model_fields_set:
            _dict['endpointType'] = None

        # set to None if metadata_endpoint_url (nullable) is None
        # and model_fields_set contains the field
        if self.metadata_endpoint_url is None and "metadata_endpoint_url" in self.model_fields_set:
            _dict['metadataEndpointUrl'] = None

        # set to None if password (nullable) is None
        # and model_fields_set contains the field
        if self.password is None and "password" in self.model_fields_set:
            _dict['password'] = None

        # set to None if soap_endpoint_url (nullable) is None
        # and model_fields_set contains the field
        if self.soap_endpoint_url is None and "soap_endpoint_url" in self.model_fields_set:
            _dict['soapEndpointUrl'] = None

        # set to None if username (nullable) is None
        # and model_fields_set contains the field
        if self.username is None and "username" in self.model_fields_set:
            _dict['username'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SfdcSourceRegistrationParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "authToken": obj.get("authToken"),
            "callbackUrl": obj.get("callbackUrl"),
            "concurrentApiRequestsLimit": obj.get("concurrentApiRequestsLimit"),
            "consumerKey": obj.get("consumerKey"),
            "consumerSecret": obj.get("consumerSecret"),
            "dailyApiLimit": obj.get("dailyApiLimit"),
            "endpoint": obj.get("endpoint"),
            "endpointType": obj.get("endpointType"),
            "metadataEndpointUrl": obj.get("metadataEndpointUrl"),
            "password": obj.get("password"),
            "soapEndpointUrl": obj.get("soapEndpointUrl"),
            "username": obj.get("username")
        })
        return _obj


