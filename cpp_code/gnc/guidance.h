// Copyright [2026] Purdue National Security and Defense Society
#ifndef NSDS_COUNTER_UAS_CPP_CODE_GNC_GUIDANCE_H_
#define NSDS_COUNTER_UAS_CPP_CODE_GNC_GUIDANCE_H_

#include <vector>

#include "utility/math/Math.h"

// Forward Declarations
namespace util::datatypes {
struct TargetPackage;
}

namespace gnc {

/**
  * @class GuidanceEngine
  * @brief Handles the guidance logic for the C-UAS GNC system.
  * 
  * The GuidanceEngine is responsible for receiving target packages and determining what the turret should aim at. The GuidanceEngine
  * must also determine what the ballistic effects of the current projectile package will be, and calculate the necessary offsets
  * to hit the chosen target.
  */
class GuidanceEngine {
  public:
    GuidanceEngine() = default;
    GuidanceEngine(const GuidanceEngine&) = delete;
    ~GuidanceEngine() = default;
    GuidanceEngine& operator=(const GuidanceEngine&) = delete;

    /**
     * @brief Guidance engine entry point. Receives a list of target packages and determines which to aim at and applies a ballistic lead offset.
     * @param target_packages a vector of target packages for processing.
     * @return The absolute sentry target statevector to aim at.
     */
    [[nodiscard]] util::math::Vector3d determine_target_statevector(const std::vector<util::datatypes::TargetPackage>& target_packages) const noexcept;
};

}  // namespace gnc

#endif  // NSDS_COUNTER_UAS_CPP_CODE_GNC_GUIDANCE_H_
