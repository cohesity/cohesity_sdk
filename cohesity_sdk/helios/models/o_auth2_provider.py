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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from cohesity_sdk.helios.models.o_auth_audience import OAuthAudience
from typing import Optional, Set
from typing_extensions import Self

class OAuth2Provider(BaseModel):
    """
    OAuth 2 provider
    """ # noqa: E501
    audiences: Optional[Annotated[List[OAuthAudience], Field(min_length=1, max_length=50)]] = Field(description="Specifies the audiences of the configuration. This is used for validation. We will check this against the 'aud' field sent in the JWT at authorization time and if they do not match against at least one of the elements in this list, then authentication will fail. We will also check the 'clientIds' under the specified audience to make sure it matches the 'appid' in the token.")
    polling_frequency_mins: Optional[Annotated[int, Field(le=10080, strict=True, ge=1)]] = Field(default=1440, description="Specifies the number of minutes the cluster should wait before polling for a new public key. Default value is 1440 (24 hours).", alias="pollingFrequencyMins")
    public_key_url: Optional[StrictStr] = Field(description="Specifies the URL to poll for the public key.", alias="publicKeyUrl")
    __properties: ClassVar[List[str]] = ["audiences", "pollingFrequencyMins", "publicKeyUrl"]

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
        """Create an instance of OAuth2Provider from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in audiences (list)
        _items = []
        if self.audiences:
            for _item_audiences in self.audiences:
                if _item_audiences:
                    _items.append(_item_audiences.to_dict())
            _dict['audiences'] = _items
        # set to None if audiences (nullable) is None
        # and model_fields_set contains the field
        if self.audiences is None and "audiences" in self.model_fields_set:
            _dict['audiences'] = None

        # set to None if polling_frequency_mins (nullable) is None
        # and model_fields_set contains the field
        if self.polling_frequency_mins is None and "polling_frequency_mins" in self.model_fields_set:
            _dict['pollingFrequencyMins'] = None

        # set to None if public_key_url (nullable) is None
        # and model_fields_set contains the field
        if self.public_key_url is None and "public_key_url" in self.model_fields_set:
            _dict['publicKeyUrl'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OAuth2Provider from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "audiences": [OAuthAudience.from_dict(_item) for _item in obj["audiences"]] if obj.get("audiences") is not None else None,
            "pollingFrequencyMins": obj.get("pollingFrequencyMins") if obj.get("pollingFrequencyMins") is not None else 1440,
            "publicKeyUrl": obj.get("publicKeyUrl")
        })
        return _obj


