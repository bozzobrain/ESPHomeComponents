#pragma once



#include "esphome/core/component.h"
#include "esphome/components/output/float_output.h"

namespace esphome {
namespace tas5806volume {


class TAS5806Volume : public Component, public output::FloatOutput {
 public:
  TAS5806Volume()  {}
  
  
  const optional<float> &get_volume() const { return volume_; }
 protected:
  void write_state(float state) override;
 private: 
  float volume_ = 50.0f;
  bool update_ = false;


};

}  // namespace tas5806volume
}  // namespace esphome