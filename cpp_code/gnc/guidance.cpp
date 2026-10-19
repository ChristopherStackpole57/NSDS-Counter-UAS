// Copyright [2026] Purdue National Security and Defense Society
#include "utility/datatypes/target_package.h"

#include "gnc/guidance.h"

namespace gnc {

using TargetPackage = util::datatype::TargetPackage;

GuidanceEngine::GuidanceEngine() {}

util::math::Vector3d GuidanceEngine::determine_target_statevector(const std::vector<TargetPackage>& target_packages) const noexcept {
  util::math::Vector3d target_statevector;

  // Run GuidanceEngine

  return target_statevector;
}

}  // namespace gnc
