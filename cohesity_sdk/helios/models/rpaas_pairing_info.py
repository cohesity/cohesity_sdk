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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.pairing_status import PairingStatus
from typing import Optional, Set
from typing_extensions import Self

class RpaasPairingInfo(BaseModel):
    """
    Holds the RPaaS Vault Information.
    """ # noqa: E501
    cluster_id: Optional[StrictInt] = Field(default=None, description="Cluster ID configured for the region.", alias="clusterId")
    cluster_incarnation_id: Optional[StrictInt] = Field(default=None, description="Cluster Incarnation ID configured for the region.", alias="clusterIncarnationId")
    pairing_status: Optional[PairingStatus] = Field(default=None, alias="pairingStatus")
    vault_id: Optional[StrictInt] = Field(default=None, description="Specifies the vault ID associated with the region.", alias="vaultId")
    __properties: ClassVar[List[str]] = ["clusterId", "clusterIncarnationId", "pairingStatus", "vaultId"]

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
        """Create an instance of RpaasPairingInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of pairing_status
        if self.pairing_status:
            _dict['pairingStatus'] = self.pairing_status.to_dict()
        # set to None if cluster_id (nullable) is None
        # and model_fields_set contains the field
        if self.cluster_id is None and "cluster_id" in self.model_fields_set:
            _dict['clusterId'] = None

        # set to None if cluster_incarnation_id (nullable) is None
        # and model_fields_set contains the field
        if self.cluster_incarnation_id is None and "cluster_incarnation_id" in self.model_fields_set:
            _dict['clusterIncarnationId'] = None

        # set to None if vault_id (nullable) is None
        # and model_fields_set contains the field
        if self.vault_id is None and "vault_id" in self.model_fields_set:
            _dict['vaultId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RpaasPairingInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clusterId": obj.get("clusterId"),
            "clusterIncarnationId": obj.get("clusterIncarnationId"),
            "pairingStatus": PairingStatus.from_dict(obj["pairingStatus"]) if obj.get("pairingStatus") is not None else None,
            "vaultId": obj.get("vaultId")
        })
        return _obj


