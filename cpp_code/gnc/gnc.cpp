#include "gnc.h"

namespace gnc {

GNCEngine::GNCEngine()
  : control_engine(0, 0, 0) {}

void GNCEngine::receive_target_packages(const std::vector<TargetPackage> target_packages) noexcept {
  return;
}

}  // namespace gnc