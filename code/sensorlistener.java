 public class MagneticWavesListener implements SensorEventListener {

    private Collector<MagneticWave> collector;
    private long currentTime;
    private long recordingRate = -1;

    public MagneticWavesListener(Collector<MagneticWave> collector)
    {
        this.collector = collector;
        this.currentTime = SystemClock.elapsedRealtime();
    }
    
    public MagneticWavesListener(Collector<MagneticWave> collector, long recordingRate)
    {
        this.collector = collector;
        this.recordingRate = recordingRate;
        this.currentTime = SystemClock.elapsedRealtime();
    }

    @Override
    public void onSensorChanged(SensorEvent event)
    {
        if(recordingRate == -1 || abs(SystemClock.elapsedRealtime() - currentTime) > recordingRate  )
        {
            float[] waveValues = event.values;
            MagneticWave mw = extractWave(waveValues);
            collector.collect(mw);
            currentTime = SystemClock.elapsedRealtime();
        }
    }

    private MagneticWave extractWave(float[] waveValues)
    {
        Double x = (double) waveValues[0];
        Double y = (double) waveValues[1];
        Double z = (double) waveValues[2];
        return new MagneticWave(x,y,z);
    }
}
