#// TODO: WTF is going on here?!?
#// Volume control (ramping)
static inline u16 ADPCM_Vol(u16 vol, u16 delta)
{
        int x = vol;
        if (delta && delta < 0x5000)
                x += delta * 20 * 8; // unsure what the right step is
                //x += 1 * 20 * 8;
        else if (delta && delta > 0x5000)
                //x -= (0x10000 - delta); // this is to small, it's often 1
                x -= (0x10000 - delta) * 20 * 16; // if this was 20 * 8 the sounds in Fire Emblem and Paper Mario
                        // did not have time to go to zero before the were closed
                //x -= 1 * 20 * 16;

         // make lower limits
        if (x < 0) x = 0;
        //if (pb.mixer_control < 1000 && x < pb.mixer_control) x = pb.mixer_control; // does this make
                // any sense?

        // make upper limits
        //if (mixer_control > 1000 && x > mixer_control) x = mixer_control; // maybe mixer_control also
                // has a volume target?
        //if (x >= 0x7fff) x = 0x7fff; // this seems a little high
        //if (x >= 0x4e20) x = 0x4e20; // add a definitive limit at 20 000
        if (x >= 0x8000) x = 0x8000; // clamp to 32768;
        return x; // update volume
}

#Part of the old AX HLE implementation. The actual correct implementation of this function would be:
#return vol + delta;


#What language is this? Uses // for comments, not #. Also makes use of the curly braces.
#Still, it's fairly understandable to me, even if it's not in Python.

# "&" is a bit operation "and". ("Bit operation?")