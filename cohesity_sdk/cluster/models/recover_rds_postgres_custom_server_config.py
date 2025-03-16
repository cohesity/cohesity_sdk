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
from cohesity_sdk.cluster.models.credentials import Credentials
from cohesity_sdk.cluster.models.recovery_object_identifier import RecoveryObjectIdentifier
from typing import Optional, Set
from typing_extensions import Self

class RecoverRDSPostgresCustomServerConfig(BaseModel):
    """
    Specifies the configuration for recovering RDS Postgres instance to the known target.
    """ # noqa: E501
    ip: StrictStr = Field(description="Specifies the Ip in which to deploy the Rds instance.")
    port: Optional[StrictInt] = Field(description="Specifies the port to use to connect to the server.")
    region: RecoveryObjectIdentifier
    standard_credentials: Credentials = Field(alias="standardCredentials")
    __properties: ClassVar[List[str]] = ["ip", "port", "region", "standardCredentials"]

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
        """Create an instance of RecoverRDSPostgresCustomServerConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of region
        if self.region:
            _dict['region'] = self.region.to_dict()
        # override the default output from pydantic by calling `to_dict()` of standard_credentials
        if self.standard_credentials:
            _dict['standardCredentials'] = self.standard_credentials.to_dict()
        # set to None if port (nullable) is None
        # and model_fields_set contains the field
        if self.port is None and "port" in self.model_fields_set:
            _dict['port'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecoverRDSPostgresCustomServerConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ip": obj.get("ip"),
            "port": obj.get("port"),
            "region": RecoveryObjectIdentifier.from_dict(obj["region"]) if obj.get("region") is not None else None,
            "standardCredentials": Credentials.from_dict(obj["standardCredentials"]) if obj.get("standardCredentials") is not None else None
        })
        return _obj


