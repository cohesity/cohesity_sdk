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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Set
from typing_extensions import Self

class SearchPublicFolderRequestParams(BaseModel):
    """
    Specifies the request parameters to search for Public Folder items.
    """ # noqa: E501
    bcc_recipient_addresses: Optional[List[Annotated[str, Field(strict=True)]]] = Field(default=None, description="Filters the public folder items which are sent to specified email addresses in BCC.", alias="bccRecipientAddresses")
    cc_recipient_addresses: Optional[List[Annotated[str, Field(strict=True)]]] = Field(default=None, description="Filters the public folder items which are sent to specified email addresses in CC.", alias="ccRecipientAddresses")
    has_attachment: Optional[StrictBool] = Field(default=None, description="Filters the public folder items which have attachment.", alias="hasAttachment")
    received_end_time_secs: Optional[StrictInt] = Field(default=None, description="Specifies the end time in Unix timestamp epoch in seconds where the received time of the public folder items is less than specified value.", alias="receivedEndTimeSecs")
    received_start_time_secs: Optional[StrictInt] = Field(default=None, description="Specifies the start time in Unix timestamp epoch in seconds where the received time of the public folder item is more than specified value.", alias="receivedStartTimeSecs")
    recipient_addresses: Optional[List[Annotated[str, Field(strict=True)]]] = Field(default=None, description="Filters the public folder items which are sent to specified email addresses.", alias="recipientAddresses")
    search_string: Optional[StrictStr] = Field(default=None, description="Specifies the search string to filter the items. User can specify a wildcard character '*' as a suffix to a string where all item names are matched with the prefix string.", alias="searchString")
    sender_address: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Filters the public folder items which are received from specified user's email address.", alias="senderAddress")
    types: Optional[List[StrictStr]] = Field(default=None, description="Specifies a list of public folder item types. Only items within the given types will be returned.")
    __properties: ClassVar[List[str]] = ["bccRecipientAddresses", "ccRecipientAddresses", "hasAttachment", "receivedEndTimeSecs", "receivedStartTimeSecs", "recipientAddresses", "searchString", "senderAddress", "types"]

    @field_validator('sender_address')
    def sender_address_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\S+@\S+.\S+$", value):
            raise ValueError(r"must validate the regular expression /^\S+@\S+.\S+$/")
        return value

    @field_validator('types')
    def types_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['Calendar', 'Contact', 'Post', 'Folder', 'Task', 'Journal', 'Note']):
                raise ValueError("each list item must be one of ('Calendar', 'Contact', 'Post', 'Folder', 'Task', 'Journal', 'Note')")
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
        """Create an instance of SearchPublicFolderRequestParams from a JSON string"""
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
        # set to None if bcc_recipient_addresses (nullable) is None
        # and model_fields_set contains the field
        if self.bcc_recipient_addresses is None and "bcc_recipient_addresses" in self.model_fields_set:
            _dict['bccRecipientAddresses'] = None

        # set to None if cc_recipient_addresses (nullable) is None
        # and model_fields_set contains the field
        if self.cc_recipient_addresses is None and "cc_recipient_addresses" in self.model_fields_set:
            _dict['ccRecipientAddresses'] = None

        # set to None if has_attachment (nullable) is None
        # and model_fields_set contains the field
        if self.has_attachment is None and "has_attachment" in self.model_fields_set:
            _dict['hasAttachment'] = None

        # set to None if received_end_time_secs (nullable) is None
        # and model_fields_set contains the field
        if self.received_end_time_secs is None and "received_end_time_secs" in self.model_fields_set:
            _dict['receivedEndTimeSecs'] = None

        # set to None if received_start_time_secs (nullable) is None
        # and model_fields_set contains the field
        if self.received_start_time_secs is None and "received_start_time_secs" in self.model_fields_set:
            _dict['receivedStartTimeSecs'] = None

        # set to None if recipient_addresses (nullable) is None
        # and model_fields_set contains the field
        if self.recipient_addresses is None and "recipient_addresses" in self.model_fields_set:
            _dict['recipientAddresses'] = None

        # set to None if search_string (nullable) is None
        # and model_fields_set contains the field
        if self.search_string is None and "search_string" in self.model_fields_set:
            _dict['searchString'] = None

        # set to None if sender_address (nullable) is None
        # and model_fields_set contains the field
        if self.sender_address is None and "sender_address" in self.model_fields_set:
            _dict['senderAddress'] = None

        # set to None if types (nullable) is None
        # and model_fields_set contains the field
        if self.types is None and "types" in self.model_fields_set:
            _dict['types'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SearchPublicFolderRequestParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bccRecipientAddresses": obj.get("bccRecipientAddresses"),
            "ccRecipientAddresses": obj.get("ccRecipientAddresses"),
            "hasAttachment": obj.get("hasAttachment"),
            "receivedEndTimeSecs": obj.get("receivedEndTimeSecs"),
            "receivedStartTimeSecs": obj.get("receivedStartTimeSecs"),
            "recipientAddresses": obj.get("recipientAddresses"),
            "searchString": obj.get("searchString"),
            "senderAddress": obj.get("senderAddress"),
            "types": obj.get("types")
        })
        return _obj


