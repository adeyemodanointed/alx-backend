function createPushNotificationsJobs (jobs, queue) {
  if (!(jobs instanceof Array)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((job) => {
    const aJob = queue.create('push_notification_code_3', job)
      .save((error) => {
        if (!error) {
          console.log(`Notification job created: ${aJob.id}`);
        }
      });

    aJob.on('complete', (result) => {
      console.log(`Notification job ${job.id} completed`);
    });

    aJob.on('failed', (error) => {
      console.log(`Notification job JOB_ID failed: ${error}`);
    });

    aJob.on('progress', (progress, data) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  });
}

module.exports = createPushNotificationsJobs;
