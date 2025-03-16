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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.oracle_db_channel import OracleDbChannel
from typing import Optional, Set
from typing_extensions import Self

class OracleProtectionGroupDbParams(BaseModel):
    """
    Specifies the parameters of individual databases to create Oracle Protection Group.
    """ # noqa: E501
    database_id: Optional[StrictInt] = Field(default=None, description="Specifies the id of the Oracle database.", alias="databaseId")
    database_name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the Oracle database.", alias="databaseName")
    db_channels: Optional[List[OracleDbChannel]] = Field(default=None, description="Specifies the Oracle database node channels info. If not specified, the default values assigned by the server are applied to all the databases.", alias="dbChannels")
    __properties: ClassVar[List[str]] = ["databaseId", "databaseName", "dbChannels"]

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
        """Create an instance of OracleProtectionGroupDbParams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "database_name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in db_channels (list)
        _items = []
        if self.db_channels:
            for _item_db_channels in self.db_channels:
                if _item_db_channels:
                    _items.append(_item_db_channels.to_dict())
            _dict['dbChannels'] = _items
        # set to None if database_id (nullable) is None
        # and model_fields_set contains the field
        if self.database_id is None and "database_id" in self.model_fields_set:
            _dict['databaseId'] = None

        # set to None if database_name (nullable) is None
        # and model_fields_set contains the field
        if self.database_name is None and "database_name" in self.model_fields_set:
            _dict['databaseName'] = None

        # set to None if db_channels (nullable) is None
        # and model_fields_set contains the field
        if self.db_channels is None and "db_channels" in self.model_fields_set:
            _dict['dbChannels'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OracleProtectionGroupDbParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "databaseId": obj.get("databaseId"),
            "databaseName": obj.get("databaseName"),
            "dbChannels": [OracleDbChannel.from_dict(_item) for _item in obj["dbChannels"]] if obj.get("dbChannels") is not None else None
        })
        return _obj


